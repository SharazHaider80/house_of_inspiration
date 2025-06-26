import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.inquiry.view import router as inquiry_router

app = FastAPI(
    title="HOI Inquiry API",
    description="A FastAPI-based bot to help customers with inquiries.",
    version="1.0.0"
)

# CORS settings
origins = [
    "https://www.homeofinspiration.ch",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "OPTIONS", "GET"],  # include GET if needed for your endpoints
    allow_headers=["Content-Type"],
)

# Register Inquiry API
app.include_router(inquiry_router, prefix="/api", tags=["inquiry"])

@app.get("/")
async def root():
    return {"message": "Welcome to the LLM Inquiry API. Use Post: /api/inquiry?query=your_query  or Get: /api/greeting"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1
    )
