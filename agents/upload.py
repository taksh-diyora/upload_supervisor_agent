from typing import Dict
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from utils.llm_factory import get_llm
from utils.config import UPLOAD_AGENT_TEMPERATURE

llm = get_llm(temperature=UPLOAD_AGENT_TEMPERATURE)

def upload_agent(state: Dict):
    user_question = state["messages"][-1].content
    document_text = state.get("document_text")

    # Safety check
    if not document_text:
        return {
            "messages": [
                AIMessage(
                    content="No PDF has been uploaded yet. Please upload a PDF first."
                )
            ]
        }

    system_prompt = """
You are a document-based assistant.

Rules:
- Answer ONLY using the provided document context
- If the answer is not found, say:
  "The uploaded document does not contain this information."
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=f"""
Document Context:
{document_text}

User Question:
{user_question}
"""
        ),
    ]

    response = llm.invoke(messages).content.strip()

    return {
        "messages": [AIMessage(content=response)]
    }
