from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config.llm_config import LLMConfig

def create_seo_chain():
    """Create a chain to generate SEO metadata"""
    
    seo_prompt = PromptTemplate.from_template(
        "Generate SEO metadata for a blog post about '{topic}'.\n\n"
        "Blog Outline:\n{outline}\n\n"
        "Keywords: {keywords}\n\n"
        "Provide:\n"
        "1. SEO Title (max 60 characters)\n"
        "2. Meta Description (max 160 characters)\n"
        "3. 5 SEO Tags\n"
        "4. URL Slug\n\n"
        "Format as JSON with keys: seo_title, meta_description, tags, url_slug\n\n"
        "SEO Metadata:"
    )
    
    llm = LLMConfig.get_structured_llm()
    
    chain = (
        {
            "topic": RunnablePassthrough(),
            "outline": RunnablePassthrough(),
            "keywords": RunnablePassthrough()
        }
        | seo_prompt
        | llm
    )
    
    return chain