# query_data.py

import os
from dotenv import load_dotenv
from config import llm  # Gemini LLM instance from config.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import warnings
import gradio as gr

warnings.filterwarnings("ignore", category=FutureWarning, module="torch.nn.modules.module")

# Load environment variables
print("🔄 Loading environment variables from .env...")
load_dotenv()

# Initialize HuggingFace Embeddings
print("🧬 Initializing embeddings for FAISS compatibility...")
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print("✅ Embeddings ready for FAISS loading.")

# Load FAISS vectorstore
print("📂 Loading vector database from 'vectorstore'...")
db = FAISS.load_local("vectorstore", embedding, allow_dangerous_deserialization=True)
print("✅ Vector database loaded.")

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff",
    return_source_documents=True
)

# Function to handle QA + sources
def ask_question(query):
    print(f"❓ User asked: {query}")
    result = qa_chain.invoke({"query": query})

    answer = result["result"]
    sources = result["source_documents"]

    # Format sources
    formatted_sources = "\n\n".join(
        f"📄 **Source {i+1}**:\n{doc.page_content[:500]}..." for i, doc in enumerate(sources)
    )

    return answer, formatted_sources

# CLI mode
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        query = input("❓ Enter your question: ")
        answer, sources = ask_question(query)

        print("\n📝 Answer:\n", answer)
        print("\n📚 Source Documents:\n", sources)

    else:
        print("🌐 Launching Web UI...")
        interface = gr.Interface(
            fn=ask_question,
            inputs=gr.Textbox(lines=2, placeholder="Ask a question about the articles..."),
            outputs=[
                gr.Textbox(label="📝 Answer"),
                gr.Textbox(label="📚 Source Documents")
            ],
            title="RAG QA System with Gemini + FAISS",
            description="Ask questions based on the embedded news articles. Powered by LangChain + Gemini + FAISS."
        )
        interface.launch()
