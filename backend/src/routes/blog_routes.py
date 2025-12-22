from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import json

router = APIRouter(prefix="/api", tags=["blog"])

class BlogRequest(BaseModel):
    topic: str
    tone: Optional[str] = "professional"
    length: Optional[str] = "medium"

class BlogResponse(BaseModel):
    topic: str
    keywords: str
    outline: str
    seo_metadata: dict
    generated_at: str

@router.get("/test")
async def test_endpoint():
    return {"message": "✅ Backend connected successfully!", "status": "active"}

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Blog Generator API"}

@router.post("/generate-blog", response_model=BlogResponse)
async def generate_blog(request: BlogRequest):
    try:
        # MOCK DATA - Remove when you add OpenAI API key
        keywords = f"mock, test, {request.topic}, keywords, example"
        outline = f"""# {request.topic.title()}: A Comprehensive Guide

## Introduction
This is a MOCK blog post about {request.topic}. To get real AI-generated content, add your OpenAI API key.

## Main Sections
1. Understanding {request.topic}
2. Key Applications
3. Future Trends
4. Practical Examples

## Conclusion
{request.topic} continues to evolve and impact our world."""
        
        seo_metadata = {
            "seo_title": f"Learn About {request.topic} - Complete Guide",
            "meta_description": f"This guide covers everything you need to know about {request.topic}.",
            "tags": [request.topic, "guide", "tutorial", "education"],
            "url_slug": f"guide-to-{request.topic.lower().replace(' ', '-')}"
        }
        
        return BlogResponse(
            topic=request.topic,
            keywords=keywords,
            outline=outline,
            seo_metadata=seo_metadata,
            generated_at=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating blog: {str(e)}")