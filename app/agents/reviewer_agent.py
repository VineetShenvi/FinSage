from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.utils.prompts import REVIEW_PROMPT, REASONING_PROMPT

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(temperature=0)

def reviewer_agent(state):
    content = (
        state["financial_analysis"] + "\n" + state["thesis"]
    )

    prompt = PromptTemplate.from_template(REVIEW_PROMPT)
    response = llm.invoke(prompt.format(content=content))
    print("Reviewer Agent response:")
    print(response.content)

    prompt = PromptTemplate.from_template(REASONING_PROMPT)
    response1 = llm.invoke(prompt.format(content=content))
    print("Reviewer Agent response:")
    print(response1.content)

    state["approved"] = "YES" in response.content.upper()
    return state
