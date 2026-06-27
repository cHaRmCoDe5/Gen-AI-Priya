from dotenv import load_dotenv
import os

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Create Embedding Model
# -----------------------------
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=api_key
)

print("✅ OpenAI Embedding Model Loaded")

# -----------------------------
# Sample Data
# -----------------------------
texts = [
    "Python is a programming language.",
    "Streamlit is used to build web apps.",
    "Dogs are friendly animals.",
    "Cats like to sleep a lot."
]

# -----------------------------
# Create FAISS Vector Store
# -----------------------------
vector_store = FAISS.from_texts(texts, embeddings)

print("✅ Vector Store Created")

# -----------------------------
# Similarity Search
# -----------------------------
query = "Tell me about pets"

results = vector_store.similarity_search(query, k=2)

print("\nTop Matches:")
for doc in results:
    print("-", doc.page_content)

# -----------------------------
# Save Vector Store
# -----------------------------
vector_store.save_local("my_store")

print("\n✅ Vector Store Saved")

# -----------------------------
# Load Vector Store
# -----------------------------
loaded_store = FAISS.load_local(
    "my_store",
    embeddings,
    allow_dangerous_deserialization=True
)

print("✅ Vector Store Loaded")

# -----------------------------
# Search Again
# -----------------------------
results = loaded_store.similarity_search("Tell me about animals", k=2)

print("\nTop Matches After Loading:")
for doc in results:
    print("-", doc.page_content)