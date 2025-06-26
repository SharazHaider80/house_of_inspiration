# app/src/inquiry/view.py

from fastapi import APIRouter, HTTPException
from src.inquiry.service import generate_llm_response  # Correct import path

router = APIRouter()

@router.post("/inquiry/")
async def inquire(query: str):
    try:
        response = generate_llm_response(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/greeting/")
async def greeting():
    try:
        message = "Hi, I’m the HOI Bot. I can guide you through booking sessions, share information about Ester and the Home of Inspiration, and help you explore our offerings. How can I help you today?"
        return {"response": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))