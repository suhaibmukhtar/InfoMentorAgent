from langchain.agents import AgentExecutor, create_react_agent
import sys
from exception import CustomException
import os
from langchain_community.document_loaders import YoutubeLoader
from langgraph.checkpoint.sqlite import SqliteSaver
import uuid
from langchain_core.messages import HumanMessage


def execute(agent, query, thread_id):
   config = {"configurable": {"thread_id": thread_id}}
   response = agent.invoke({'messages': [HumanMessage(query)]}, config=config)
   for message in response["messages"]:
       print(
           f"{message.__class__.__name__}: {message.content}"
       )  
       print("-" * 20, end="\n")
   return response

def get_agent(chat_model, tools, prompt):
    """
    Returns an agent with LangSmith tracing enabled
    
    Args:
        chat_model: The language model to use
        tools: List of tools available to the agent
        prompt: The prompt template for the agent
        
    Returns:
        AgentExecutor: Configured agent executor
    """
    try:
        my_uuid = uuid.uuid4()
        memory = SqliteSaver.from_conn_string(f':agent_history:{my_uuid}')
        config = {'configurable': {'thread_id': my_uuid}}   
        # Create the agent with tracing configuration
        agent = create_react_agent(chat_model, tools, prompt, config=config)
        
        # Configure the agent executor with tracing
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            checkpointer=memory,
            tags=["education_assistant"],
            metadata={
                "project": os.getenv("LANGCHAIN_PROJECT", "education_bot"),
                "agent_type": "react",
                "purpose": "student_assistance"
            }
        )
        return agent_executor
    except Exception as e:
        raise CustomException(e, sys)
    
    

agent = create_react_agent(chat_model, tools, checkpointer=memory, state_modifier=system_prompt)