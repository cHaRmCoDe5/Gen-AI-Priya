import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

# ---------------- ENV ----------------
load_dotenv()

# ---------------- LANGCHAIN IMPORTS ----------------
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------- UI ----------------
st.set_page_config(page_title="FAISS RAG Chatbot", page_icon="📄")
st.title("📄 FAISS RAG PDF Chatbot")
st.write("Upload a PDF and ask questions from it.")

# ---------------- API KEY CHECK ----------------
if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY not found in .env file")
    st.stop()

# ---------------- SESSION STATE ----------------
if "db" not in st.session_state:
    st.session_state.db = None

if "file_name" not in st.session_state:
    st.session_state.file_name = None


# ---------------- UPLOAD PDF ----------------
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    if st.session_state.file_name != uploaded_file.name:

        with st.status("Processing PDF..."):

            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                file_path = tmp.name

            st.write("Reading PDF...")
            loader = PyPDFLoader(file_path)
            docs = loader.load()

            text = "".join([d.page_content for d in docs])

            if not text.strip():
                st.error("No readable text found. PDF may be scanned (needs OCR).")
                st.stop()

            st.write("Splitting text...")
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(docs)

            st.write("Creating embeddings...")
            embeddings = OpenAIEmbeddings()

            st.write("Building FAISS vector store...")
            db = FAISS.from_documents(chunks, embeddings)

            st.session_state.db = db
            st.session_state.file_name = uploaded_file.name

            os.remove(file_path)

            st.success("PDF processed successfully!")


# ---------------- CHAT SECTION ----------------
if st.session_state.db:

    st.success("Ready! Ask your question 👇")

    question = st.text_input("Ask something from your PDF")

    if question:

        retriever = st.session_state.db.as_retriever(search_kwargs={"k": 3})

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        prompt = ChatPromptTemplate.from_template("""
        You are a helpful assistant.

        Use ONLY the context below to answer the question.
        If the answer is not in the context, say "Not found in document".

        Context:
        {context}

        Question:
        {question}
        """)

        # ✅ MODERN LANGCHAIN RETRIEVAL
        docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in docs])

        formatted_prompt = prompt.invoke({
            "context": context,
            "question": question
        })

        with st.spinner("Thinking..."):
            response = llm.invoke(formatted_prompt)

        st.subheader("Answer")
        st.write(response.content)

else:
    st.info("Upload a PDF to start chatting.")