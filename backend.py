import os
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ------------------------
# API
# ------------------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ------------------------
# Load PDFs
# ------------------------
def load_vector_db():

    all_docs = []
    pdf_folder = "pdfs"

    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_folder, file))
            docs = loader.load()
            all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(all_docs)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embedding)

    return vector_db


vector_db = load_vector_db()

# ------------------------
# Manager Agent
# ------------------------
def manager_agent(question):

    q = question.lower()

    if "quiz" in q or "mcq" in q:
        return "QUIZ"

    if "rule" in q or "policy" in q:
        return "RAG"

    return "TEACH"

# ------------------------
# RAG Agent
# ------------------------
def rag_agent(question):

    docs = vector_db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer strictly from context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ------------------------
# Teacher Agent
# ------------------------
def teacher_agent(text):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Explain simply."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content

# ------------------------
# Quiz Agent
# ------------------------
def quiz_agent(topic):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Generate 5 MCQs with answers."},
            {"role": "user", "content": topic}
        ]
    )

    return response.choices[0].message.content

# ------------------------
# Main Router
# ------------------------
def handle_query(question):

    decision = manager_agent(question)

    if decision == "RAG":
        return rag_agent(question), decision

    elif decision == "QUIZ":
        return quiz_agent(question), decision

    else:
        return teacher_agent(question), decision

# # ------------------------
# # Chat Loop
# # ------------------------
# while True:

#     question = input("\nAsk Question (exit to stop): ")

#     if question.lower() == "exit":
#         break

#     decision = manager_agent(question)

#     print("\nManager Selected:", decision)

#     if decision == "RAG":
#         result = rag_agent(question)

#     elif decision == "QUIZ":
#         result = quiz_agent(question)

#     else:
#         result = teacher_agent(question)

#     print("\n✅ Response:\n")
#     print(result)



#         User Question
#              ↓
#    Manager Agent (Decision)
#              ↓
#┌───────────────┬───────────────┬───────────────┐
#│   RAG Agent   │ Teacher Agent │   Quiz Agent  │
#│ (PDF search)  │ (Explain)     │ (MCQs)        │
#└───────────────┴───────────────┴───────────────┘
#              ↓
#         Final Answer