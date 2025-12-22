import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMConfig:
    """Configure and initialize LLMs for different tasks"""
    
    @staticmethod
    def get_primary_llm():
        """Main LLM for content generation"""
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    @staticmethod
    def get_creative_llm():
        """More creative LLM for titles and intros"""
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.9,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    @staticmethod
    def get_structured_llm():
        """Less creative LLM for outlines and SEO"""
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        )