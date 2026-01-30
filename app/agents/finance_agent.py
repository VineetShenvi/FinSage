from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from app.utils.prompts import FINANCE_PROMPT

llm = ChatOpenAI(temperature=0)


def finance_agent(state):
    retriever = state["retriever"]
    docs = retriever.get_relevant_documents(state["company"])

    context = "\n".join(d.page_content for d in docs)
    prompt = PromptTemplate.from_template(FINANCE_PROMPT)

    response = llm.invoke(prompt.format(context=context, company=state["company"]))
    print("Finance Agent response:")
    print(response.content)
    state["financial_analysis"] = response.content
    return state
