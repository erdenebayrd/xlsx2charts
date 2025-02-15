from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
@app.get("/api")
async def root():
    return {"message": "Welcome to xlsx2charts API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Serve static files
app.mount("/assets", StaticFiles(directory="static/static"), name="static")

# Serve React app
@app.get("/{full_path:path}")
async def serve_react(full_path: str):
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not found")
        
    static_file = os.path.join("static", full_path)
    if os.path.exists(static_file) and not os.path.isdir(static_file):
        return FileResponse(static_file)
    
    return FileResponse("static/index.html") 