from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config.llm_config import LLMConfig

def create_outline_chain():
    """Create a chain to generate blog outline"""
    
    outline_prompt = PromptTemplate.from_template(
        "Create a detailed blog outline for topic: '{topic}'\n\n"
        "Keywords to consider: {keywords}\n\n"
        "The outline should include:\n"
        "1. Introduction section\n"
        "2. 3-5 main sections with subtopics\n"
        "3. Conclusion section\n"
        "4. Call-to-action\n\n"
        "Format the outline clearly with headings and bullet points.\n\n"
        "Outline:"
    )
    
    llm = LLMConfig.get_structured_llm()
    
    chain = (
        {"topic": RunnablePassthrough(), "keywords": RunnablePassthrough()}
        | outline_prompt
        | llm
    )
    
    return chain