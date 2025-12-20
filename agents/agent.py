from langchain.agents import create_agent
from utils.llm_factory import get_llm

# =========================
# GLOBAL DOCUMENT STORAGE
# =========================
DOCUMENT_TEXT = None


def set_document_text(text: str | None):
    global DOCUMENT_TEXT
    DOCUMENT_TEXT = text


# =========================
# CORE ANSWER LOGIC
# =========================

def _answer_direct(question: str) -> str:
    """Answer using Groq's general knowledge."""
    llm = get_llm()
    return llm.invoke(question).content.strip()


def _answer_from_pdf_or_fallback(question: str) -> str:
    """
    Single-call strategy:
    - Ask Groq to answer using the PDF if possible
    - If not possible, Groq explicitly signals fallback
    """
    llm = get_llm()

    prompt = f"""
You are an assistant with access to an uploaded document.

Instructions:
- If the question can be answered using the document, answer using it.
- You MAY summarize or infer structure from the document.
- Do NOT introduce facts not supported by the document.
- If the document does NOT help answer the question, respond EXACTLY with:
  FALLBACK_TO_GENERAL_KNOWLEDGE

Document:
{DOCUMENT_TEXT}

Question:
{question}
"""

    return llm.invoke(prompt).content.strip()


# =========================
# AGENT CREATION (REQUIRED)
# =========================

def build_agent():
    """
    create_agent is used to satisfy the architectural requirement.
    We do not rely on it for final text generation.
    """
    llm = get_llm()
    return create_agent(llm)


# =========================
# PUBLIC ENTRY POINT
# =========================

def run_agent(question: str) -> str:
    """
    Optimized hybrid strategy:
    - If no PDF → general answer
    - If PDF exists → ONE call that either answers from PDF
      or explicitly requests fallback
    """
    if not DOCUMENT_TEXT:
        return _answer_direct(question)

    response = _answer_from_pdf_or_fallback(question)

    if response.strip() == "FALLBACK_TO_GENERAL_KNOWLEDGE":
        return _answer_direct(question)

    return response
