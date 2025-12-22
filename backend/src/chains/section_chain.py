from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config.llm_config import LLMConfig

def create_section_chain():
    """Create a chain to write individual blog sections"""
    
    section_prompt = PromptTemplate.from_template(
        "Write a comprehensive blog section about: '{section_title}'\n\n"
        "Main Topic: {topic}\n"
        "Keywords to include: {keywords}\n\n"
        "Requirements:\n"
        "- Write 2-3 paragraphs (150-200 words)\n"
        "- Include relevant keywords naturally\n"
        "- Use engaging, informative tone\n"
        "- Add examples or data where appropriate\n\n"
        "Section Content:"
    )
    
    llm = LLMConfig.get_primary_llm()
    
    chain = (
        {
            "section_title": RunnablePassthrough(),
            "topic": RunnablePassthrough(),
            "keywords": RunnablePassthrough()
        }
        | section_prompt
        | llm
    )
    
    return chain