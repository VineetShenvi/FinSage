from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from app.utils.web_search import search_web
from app.utils.web_scraper import scrape_url

llm = ChatOpenAI(temperature=0)

def research_agent(state):
    company = state["company"]

    # 1️⃣ Search the web
    query = f"Investments made by {company} reently"
    urls = search_web(query)

    print(f"Research Agent found {len(urls)} URLs.")

    # 2️⃣ Scrape content
    raw_texts = []
    for url in urls:
        text = scrape_url(url)
        if len(text) > 500:
            raw_texts.append(text)

    # 3️⃣ Chunk text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    documents = []
    for text in raw_texts:
        chunks = splitter.split_text(text)
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
