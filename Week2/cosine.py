from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np

# ------------------------------------
# Step 1: Load the embedding model
# ------------------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ------------------------------------
# Step 2: Cosine Similarity Function
# ------------------------------------
def similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# ------------------------------------
# Step 3: Create Embeddings
# ------------------------------------
text1 = "I like dogs"
text2 = "I love puppies"
text3 = "The car is fast"

v1 = embeddings.embed_query(text1)
v2 = embeddings.embed_query(text2)
v3 = embeddings.embed_query(text3)

# ------------------------------------
# Step 4: Print Similarity Scores
# ------------------------------------
print("=" * 50)
print("Sentence Similarity using LangChain Embeddings")
print("=" * 50)

print(f"\nText 1: {text1}")
print(f"Text 2: {text2}")
print(f"Text 3: {text3}")

print("\nSimilarity Scores:")
print(f"'{text1}'  vs  '{text2}' : {similarity(v1, v2):.4f}")
print(f"'{text1}'  vs  '{text3}' : {similarity(v1, v3):.4f}")

print("\nInterpretation:")
print("- A score closer to 1 means the sentences are more similar.")
print("- A score closer to 0 means they are less similar.")
print("- Negative values indicate opposite meanings (less common with sentence embeddings).")