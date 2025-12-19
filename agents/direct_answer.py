from typing import Dict
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from utils.llm_factory import get_llm
from utils.config import DIRECT_AGENT_TEMPERATURE

llm = get_llm(temperature=DIRECT_AGENT_TEMPERATURE)

def direct_answer_agent(state: Dict):
    user_question = state["messages"][-1].content

    system_prompt = """
You are a helpful assistant.

Rules:
- Answer clearly and concisely
- Do not reference documents or PDFs
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_question),
    ]

    response = llm.invoke(messages).content.strip()

    return {
        "messages": [AIMessage(content=response)]
    }
