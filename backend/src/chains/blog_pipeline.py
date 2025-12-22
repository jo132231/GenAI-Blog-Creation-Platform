from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from .keyword_chain import create_keyword_chain
from .outline_chain import create_outline_chain
from .seo_chain import create_seo_chain

def create_blog_pipeline():
    """Create the complete blog generation pipeline"""
    
    # Initialize individual chains
    keyword_chain = create_keyword_chain()
    outline_chain = create_outline_chain()
    seo_chain = create_seo_chain()
    
    # Create the main pipeline
    pipeline = (
        {"topic": RunnablePassthrough()}
        | RunnableParallel({
            "keywords": keyword_chain,
            "topic": lambda x: x["topic"]
        })
        | RunnableParallel({
            "outline": lambda x: outline_chain.invoke({
                "topic": x["topic"],
                "keywords": x["keywords"].content if hasattr(x["keywords"], 'content') else x["keywords"]
            }),
            "keywords": lambda x: x["keywords"],
            "topic": lambda x: x["topic"]
        })
        | RunnableParallel({
            "seo_metadata": lambda x: seo_chain.invoke({
                "topic": x["topic"],
                "outline": x["outline"].content if hasattr(x["outline"], 'content') else x["outline"],
                "keywords": x["keywords"].content if hasattr(x["keywords"], 'content') else x["keywords"]
            }),
            "outline": lambda x: x["outline"],
            "keywords": lambda x: x["keywords"],
            "topic": lambda x: x["topic"]
        })
    )
    
    return pipeline