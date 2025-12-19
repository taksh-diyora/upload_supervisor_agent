from typing import Dict
from langchain_core.messages import SystemMessage, HumanMessage
from utils.llm_factory import get_llm
from utils.config import SUPERVISOR_TEMPERATURE

llm = get_llm(temperature=SUPERVISOR_TEMPERATURE)

def supervisor_agent(state: Dict):
    user_message = state["messages"][-1].content

    system_prompt = """
You are a supervisor agent.

Decide which agent should handle the user request.

Agents:
- upload_agent → PDF / document-related queries
- direct_answer → general questions

Rules:
- Output ONLY one word
- No explanation
- Valid outputs:
  upload_agent
  direct_answer
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message),
    ]

    decision = llm.invoke(messages).content.strip()

    if decision not in {"upload_agent", "direct_answer"}:
        decision = "direct_answer"

    return {"route": decision}
