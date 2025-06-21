# app/src/langchain_client.py

from langchain_community.chat_models import ChatOpenAI
from src.config.config import OPENAI_API_KEY

def get_langchain_llm():
    try:
        if not OPENAI_API_KEY:
            raise ValueError("HOI_GPT_API_KEY missing. Set it in .env or environment variables.")
        
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )
        return llm

    except Exception as e:
        print(f"[Unexpected Error] {e}")
