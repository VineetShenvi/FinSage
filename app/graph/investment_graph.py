from langgraph.graph import StateGraph, END

from app.agents.research_agent import research_agent
from app.agents.finance_agent import finance_agent
from app.agents.thesis_agent import thesis_agent
from app.agents.reviewer_agent import reviewer_agent
from app.rag.faiss_store import FAISSStore

vector_store = FAISSStore()

def index_documents(state):
    vector_store.add_documents(state["documents"])
    state["retriever"] = vector_store.retriever()
    return state

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("research", research_agent)
    graph.add_node("index", index_documents)
    graph.add_node("finance", finance_agent)
    graph.add_node("thesis", thesis_agent)
    graph.add_node("review", reviewer_agent)

    graph.set_entry_point("research")

    graph.add_edge("research", "index")
    graph.add_edge("index", "finance")
    graph.add_edge("finance", "thesis")
    graph.add_edge("thesis", "review")

    def route_review(state):
        if state["approved"]:
            return END

        state["retry_count"] += 1

        if state["retry_count"] >= state["max_retries"]:
            # Stop retrying, force exit
            return END

        return "research"


    graph.add_conditional_edges("review", route_review)

    return graph.compile()
