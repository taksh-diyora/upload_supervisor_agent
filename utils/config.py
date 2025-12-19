import os

# ==============================
# LLM Configuration
# ==============================

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

SUPERVISOR_TEMPERATURE = 0.0
UPLOAD_AGENT_TEMPERATURE = 0.0
DIRECT_AGENT_TEMPERATURE = 0.3

# ==============================
# RAG (future use)
# ==============================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 4
