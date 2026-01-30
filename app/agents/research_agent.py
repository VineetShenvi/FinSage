from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.utilities import SerpAPIWrapper
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from app.utils.web_search import search_scrape

llm = ChatOpenAI(temperature=0)

def research_agent(state):
    company = state["company"]

    # 1️⃣ Search the web
    content = search_scrape(company = company)

    

    # 3️⃣ Chunk text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    documents = []
    
    chunks = splitter.split_text(content)
    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk,
                metadata={"company": company}
            )
        )

    print(f"Research Agent created {len(documents)} document chunks.")
    print("Sample document chunk:")
    if documents:
        print(documents[0].page_content[:500] + "...")  

    state["documents"] = documents
    return state
