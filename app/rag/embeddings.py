from langchain_openai import OpenAIEmbeddings
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_embeddings():
    return OpenAIEmbeddings()
