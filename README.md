# 🧠 RAG-Based Question Answering System

This project is a **Retrieval-Augmented Generation (RAG)** application built using **LangChain**, **FAISS**, **Gemini/OpenAI**, and **Gradio**. It allows users to ask questions and receive context-aware answers pulled directly from uploaded documents — along with the sources used in the answer.

## 🚀 Features

- Semantic search using vector embeddings (FAISS)
- GPT-based language model with LangChain
- PDF/Text document loader and chunker
- Interactive UI built using Gradio
- Source documents shown with the answers
- Modular and extendable code

## 📦 Setup

Clone the repository and install the dependencies using pip. It’s recommended to use a virtual environment.

```bash
git clone https://github.com/MohammedHasanMustafa/rag-app.git
cd rag-app
pip install -r requirements.txt
```

Set your API key by creating a `.env` file in the root directory:

```
GEMINI_API_KEY=your-gemini-api-key
```

## 💻 Run the App

```bash
python query_data.py
```

Once started, the Gradio UI will open in your browser where you can ask questions and receive answers with sources.

## 🧠 How It Works

1. Loads documents from the `documents/` folder.
2. Splits them into smaller chunks.
3. Generates vector embeddings for each chunk using Gemini or OpenAI embeddings.
4. Stores them in a FAISS vector database.
5. On user input:
   - Retrieves top matching chunks using semantic similarity.
   - Sends the context and user query to Gemini LLM.
   - Displays the final answer along with reference sources.

## ✨ Example Questions

You can try asking:

- What are the recent trends in AI development?
- Explain the risks of autonomous vehicles in AI applications.
- What is the significance of different bit precisions in AI chips?
- How can AI be misused in spreading misinformation?
- List some real-world applications of artificial intelligence mentioned in the text.

## 🧱 Built With

- LangChain  
- FAISS  
- Gemini (or OpenAI)  
- Gradio  

## 🛠️ Future Enhancements

- Upload PDFs and URLs dynamically  
- Deploy to Hugging Face Spaces / Streamlit Cloud  
- Feedback and rating system  
- Multilingual support  
- Add chat memory and history  
- Enable document re-indexing without restart
