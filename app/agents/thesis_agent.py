from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.utils.prompts import THESIS_PROMPT
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(temperature=0)

def thesis_agent(state):
    analysis = state["financial_analysis"]
    prompt = PromptTemplate.from_template(THESIS_PROMPT)

    response = llm.invoke(prompt.format(analysis=analysis, company=state["company"]))
    state["thesis"] = response.content
    return state
