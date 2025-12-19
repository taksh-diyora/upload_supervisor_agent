from langgraph.graph import StateGraph, START, END
from state.state import AgentState
from agents.supervisor import supervisor_agent
from agents.upload import upload_agent
from agents.direct_answer import direct_answer_agent

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("supervisor", supervisor_agent)
    builder.add_node("upload_agent", upload_agent)
    builder.add_node("direct_answer", direct_answer_agent)

    builder.add_edge(START, "supervisor")

    def route_decision(state: AgentState):
        return state["route"]

    builder.add_conditional_edges(
        "supervisor",
        route_decision,
        {
            "upload_agent": "upload_agent",
            "direct_answer": "direct_answer"
        }
    )

    builder.add_edge("upload_agent", END)
    builder.add_edge("direct_answer", END)

    return builder.compile()
