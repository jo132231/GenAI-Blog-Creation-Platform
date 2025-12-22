from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config.llm_config import LLMConfig

def create_keyword_chain():
    """Create a chain to generate keywords for a blog topic"""
    
    keyword_prompt = PromptTemplate.from_template(
        "Generate 5-7 relevant keywords for a blog post about '{topic}'.\n"
        "Consider search terms, related concepts, and long-tail keywords.\n\n"
        "Return as a comma-separated list.\n\n"
        "Keywords:"
    )
    
    llm = LLMConfig.get_structured_llm()
    
    chain = (
        {"topic": RunnablePassthrough()}
        | keyword_prompt
        | llm
    )
    
    return chain