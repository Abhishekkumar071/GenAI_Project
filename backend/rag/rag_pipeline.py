from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from langchain_huggingface import HuggingFaceEmbeddings
# GROQ_API_KEY = "Write your Groq API key here"

from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
# load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# uvicorn app:app --reload
# load vector DB
# db = FAISS.load_local("vectorstore/faiss_index", embeddings)
db = FAISS.load_local(
    "C:\\Users\\abhis\\Desktop\\personalBot\\backend\\vectorstore\\faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

client = Groq(api_key=groq_api_key)


def ask_bot(query):

    docs = db.similarity_search(query, k=2)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer using only the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content