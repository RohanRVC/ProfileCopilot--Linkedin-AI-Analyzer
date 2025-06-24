# langgraph_flow/flow_builder.py

from langgraph.graph import StateGraph
from typing import Dict, Any

# Import agents
from agents.profile_analyzer import analyze_profile
from agents.job_matcher import match_job
from agents.content_rewriter import rewrite_content

### 🔹 Define a shared state object
# Input/Output flow will pass through this shared dict
State = Dict[str, Any]

### 🔹 Node 1 – Profile Analysis
def profile_node(state: State) -> State:
    profile = state["profile"]
    analysis = analyze_profile(profile)
    state["analysis"] = analysis
    return state

### 🔹 Node 2 – Job Fit Comparison
def job_match_node(state: State) -> State:
    profile = state["profile"]
    job_title = state["job"]
    jd = state["jd"]
    match = match_job(profile, job_title, jd)
    state["match"] = match
    return state

### 🔹 Node 3 – Content Rewriting
def rewrite_node(state: State) -> State:
    profile = state["profile"]
    job_title = state["job"]
    rewrite = rewrite_content(profile, job_title)
    state["rewrite"] = rewrite
    return state

### ✅ Compile the LangGraph pipeline
def build_flow():
    sg = StateGraph(State)

    sg.add_node("analyze", profile_node)
    sg.add_node("match", job_match_node)
    sg.add_node("rewrite", rewrite_node)

    sg.set_entry_point("analyze")
    sg.add_edge("analyze", "match")
    sg.add_edge("match", "rewrite")
    sg.set_finish_point("rewrite")

    return sg.compile()
