# app/main.py

import uvicorn
from fastapi import FastAPI
from src.inquiry.view import router as inquiry_router

app = FastAPI(
    title="HOI Inquiry API",
    description="A FastAPI-based bot to help customers with inquiries.",
    version="1.0.0"
)

# Register Inquiry API
app.include_router(inquiry_router, prefix="/api", tags=["inquiry"])

@app.get("/")
async def root():
    return {"message": "Welcome to the LLM Inquiry API. Use /api/inquiry?query=your_query"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Because main.py is directly in app/
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1
    )
