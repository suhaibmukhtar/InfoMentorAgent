from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import sys
from langsmith.wrappers import wrap_openai
from exception import CustomException

load_dotenv()

def get_model()->ChatOpenAI:
    """
    Returns a chat model with the given parameters
    Args:
        None
    Returns:
        chat_model: ChatOpenAI
    """
    try:
        chat_model = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"), 
            model=os.getenv("MODEL_NAME"),
            temperature=0,
            max_tokens=600,
        )
        return chat_model
    except Exception as e:
        raise CustomException(e, sys)