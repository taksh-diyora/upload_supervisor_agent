from langchain_groq import ChatGroq
from utils.config import GROQ_MODEL

def get_llm(temperature: float = 0.0):
    return ChatGroq(
        model=GROQ_MODEL,
        temperature=temperature
    )
