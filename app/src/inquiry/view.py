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
