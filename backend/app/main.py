from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Document Intelligence API",
    description="Backend API for AI-powered document management and analysis.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Document Intelligence API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}