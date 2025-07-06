from langchain.prompts import PromptTemplate
import sys
from exception import CustomException

def get_prompt_template():
    """
    Returns a prompt template
    """
    try:
        # Create the prompt template
        template = """You are a helpful bot named Suhaib, who helps students in their studies by helping them with their doubts and questions.

        You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        {agent_scratchpad}
        """
        prompt = PromptTemplate.from_template(template)
        return prompt
    except Exception as e:
        raise CustomException(e, sys)