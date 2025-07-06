from typing import List, Dict, Any
from langchain_community.tools import WikipediaQueryRun  
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import YouTubeSearchTool  
from dotenv import load_dotenv
import os
from model import get_model
from tools import get_tools
from prompt_template import get_prompt_template
from agent import get_agent,execute
from warnings import filterwarnings
from logger import logging
from langchain_community.chat_message_histories import SQLChatMessageHistory
import sys
import re
from exception import CustomException

filterwarnings("ignore")

load_dotenv()

def main():
    """
    Main function
    """
    try:
        # get the model, tools, prompt and agent
        chat_model = get_model()
        logging.info("Model loaded successfully")
        tools = get_tools()
        logging.info("Tools loaded successfully")
        prompt = get_prompt_template()
        logging.info("Prompt loaded successfully")
        
        if not all([chat_model, tools, prompt]):
            logging.error("Failed to load required components")
            return
            
        agent_executor = get_agent(chat_model, tools, prompt)
        logging.info("Agent-executor loaded successfully")

        # Run with tracing enabled
        query = "Kashmir travel videos?"
        logging.info(f"Query: {query}")
        
        response = execute(agent_executor, query)
        logging.info(f"Response: {response}")
        
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()




