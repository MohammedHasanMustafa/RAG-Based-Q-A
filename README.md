# 🧠 RAG-Based Question Answering System

This project is a **Retrieval-Augmented Generation (RAG)** application built using **LangChain**, **FAISS**, **OpenAI**, and **Gradio**. It allows users to ask questions and receive context-aware answers pulled directly from the uploaded documents — along with sources used in the answer.

---

## 🚀 Features

- 🔍 Semantic search using vector embeddings (FAISS)
- 🧠 GPT-based language model with LangChain
- 📄 PDF/Text document loader and chunker
- 💬 Interactive UI built using Gradio
- 📚 Source documents shown with the answers
- ✅ Modular and extendable code

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-app.git
cd rag-app

2. Install Dependencies
We recommend using a virtual environment.

pip install -r requirements.txt

### 3. Set Your API Key
Create a .env file in the root directory:

GEMINI_API_KEY=your-gemini-api-key

### 🧠 How It Works

- Loads documents from the documents/ folder.

- Splits them into smaller chunks.

- Generates vector embeddings for each chunk using GEMINI.

- Stores them in a FAISS vector database.

- On user question input, it:

- Retrieves top matching chunks using cosine similarity.

- Sends the context + question to GEMINI to generate an answer.

- Displays the final answer along with the source chunks.

### 💻 Run the App

python query_data.py
This will open the Gradio interface in your browser.

### ✨ Example Questions
Here are a few examples you can try in the UI:

- "What are the recent trends in AI development?",
- "Explain the risks of autonomous vehicles in AI applications.",
- "What is the significance of different bit precisions in AI chips?",
- "How can AI be misused in spreading misinformation?",
- "List some real-world applications of artificial intelligence mentioned in the text.

### 🧱 Built With
- LangChain

- FAISS

- GEMINI

- Gradio

### 🛡️ Future Enhancements
- Add PDF/URL uploader to update knowledge base dynamically
- Connect to external knowledge sources (news, sites, etc.)
- Deploy to Hugging Face Spaces or Streamlit Cloud

Add feedback/rating system

Enable multilingual support
