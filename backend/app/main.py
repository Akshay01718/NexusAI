from fastapi import FastAPI

app = FastAPI(
    title="NexusAI API",
    description="AI-powered Software Engineering Workspace",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to NexusAI API 🚀"
    }