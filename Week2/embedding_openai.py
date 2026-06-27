from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# A small, cheap, high-quality OpenAI embedding model
openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key = api_key)

print("OpenAI embedding model is ready!")