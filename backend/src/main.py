from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import blog_routes
import uvicorn

app = FastAPI(
    title="AI Blog Generator API",
    description="Backend for generating blog content using LangChain",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(blog_routes.router)

@app.get("/")
async def root():
    return {
        "message": "AI Blog Generator API",
        "docs": "http://localhost:8000/docs",
        "endpoints": {
            "GET /api/health": "Check API health",
            "POST /api/generate-blog": "Generate blog content",
            "GET /api/test": "Test connection"
        }
    }

if __name__ == "__main__":
    print("🚀 Starting AI Blog Generator API...")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🔗 Frontend: http://localhost:3000")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)