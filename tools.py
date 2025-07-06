from typing import List, Dict, Any, Union
from langchain_community.tools import WikipediaQueryRun  
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import YouTubeSearchTool  
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.tools import tool
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
import sys
import re
import os
from exception import CustomException

    

## wikipedia search tool : makes a call to wikipedia api to get the information
@tool
def wikipedia_search(query: str) -> str:
    """
    A tool to search Wikipedia for textual information. Use this tool if you think the user's asked concept is best explained through text
    
    Args:
        query (str): The search query to look up on Wikipedia
        
    Returns:
        str: Wikipedia search results
        
    Raises:
        Exception: If the Wikipedia API call fails
    """
    try:
        wiki_api_wrapper = WikipediaAPIWrapper(
            top_k_results=1, 
            doc_content_chars_max=500
        )
        wikipedia = WikipediaQueryRun(
            description="A tool to explain things in text format. Use this tool if you think the user's asked concept is best explained through text.",
            api_wrapper=wiki_api_wrapper
        )
        return wikipedia.invoke(query)
    except Exception as e:
        return f"Error searching Wikipedia: {str(e)}"

## youtube search tool : makes a call to youtube api to get the information (no need of api key)
@tool
def youtube_search(query: str) -> List[str]:
    """
    A tool to search YouTube videos. Use this tool if you think the user's asked concept can be best explained by watching a video.
    
    Args:
        query (str): The search query to look up on YouTube
        
    Returns:
        List[str]: List of YouTube video URLs
        
    Raises:
        CustomException: If the YouTube search fails
    """
    try:
        youtube = YouTubeSearchTool(
            description="A tool to search YouTube videos. Use this tool if you think the user's asked concept can be best explained by watching a video."
        )
        response = youtube.run(query)
        url_pattern = r"https?:\/\/[^\s\)]+"
        video_urls = re.findall(url_pattern, str(response))
        
        # Return first 3 video URLs
        return video_urls[:3]
    except Exception as e:
        raise CustomException(f"Error searching YouTube: {str(e)}", sys)

# @tool
# def get_youtube_transcript(video_urls: List[str]) -> List[str]:
#     """
#     A tool to get the transcript of a YouTube video.
    
#     Args:
#         video_urls (List[str]): The URLs of the YouTube videos to get the transcript from
        
#     Returns:
#         List[str]: The transcript of the videos
        
#     Raises:
#         CustomException: If getting the transcript fails
#     """
#     try:

#         return transcriptions
#     except Exception as e:
#         raise CustomException(f"Error getting YouTube transcript: {str(e)}", sys)


@tool
def web_search(query: str) -> str:
    """
    Search the web for current information, news, and real-time data.
    Use this for recent events, current affairs, or information not on Wikipedia.
    """
    try:
        search = GoogleSerperAPIWrapper(api_key=os.getenv("SERPER_API_KEY"))
        return search.run(query)
    except Exception as e:
        raise CustomException(f"Error searching the web: {str(e)}", sys)
    
@tool
def news_search(query: str) -> str:
    """
    Get latest news articles on any topic.
    Perfect for current events, breaking news, and recent developments.
    """
    try:
        search = GoogleSerperAPIWrapper(api_key=os.getenv("SERPER_API_KEY"))
        return search.run(query)
    except Exception as e:
        raise CustomException(f"Error searching the web: {str(e)}", sys)

@tool
def wolfram_alpha_query(query: str) -> str:
    """
    Get mathematical calculations, scientific data, and computational answers.
    Perfect for math problems, physics calculations, and data analysis.
    """


def get_tools():
    """
    Returns a list of tools
    """
    try:
        # List of tools
        tools: List = [wikipedia_search, youtube_search,web_search,news_search]
        return tools
    except Exception as e:
        raise CustomException(e, sys)










