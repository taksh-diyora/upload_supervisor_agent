from typing import TypedDict, Annotated, List
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # Chat history
    messages: Annotated[List[BaseMessage], add_messages]

    # Routing decision
    route: str

    # Uploaded PDF text (None if not uploaded)
    document_text: str | None
