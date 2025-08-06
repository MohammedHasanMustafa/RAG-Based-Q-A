# create_database.py

import os
import pandas as pd
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

data_dir = "data/extracted_articles"
db_dir = "vectorstore"
metadata_file = "data/metadata.csv"

print("🚀 Starting vector DB creation with metadata...\n")

# Load metadata
print("📄 Loading metadata.csv...")
df_meta = pd.read_csv(metadata_file)

# Ensure expected column is present
if "article_file" not in df_meta.columns:
    raise ValueError("❌ 'article_file' column not found in metadata.csv.")

# Create a mapping: filename -> metadata (category)
file_to_category = dict(zip(df_meta["article_file"], df_meta["category"]))

# Load and prepare documents with metadata
print("📚 Loading articles and attaching metadata...")
documents = []

print("📁 Scanning directory:", data_dir)

for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(data_dir, filename)
        category = file_to_category.get(filename, "Unknown")  # Default to 'Unknown' if not found

        print(f"\n📄 Processing file: {filename}")
        print(f"📂 Full path: {filepath}")
        print(f"🏷️ Category from metadata: {category}")

        try:
            loader = TextLoader(filepath, encoding="utf-8")
            loaded_docs = loader.load()
            print(f"✅ Loaded {len(loaded_docs)} document(s) from {filename}")

            for doc in loaded_docs:
                doc.metadata["category"] = category
            documents.extend(loaded_docs)

        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")

print(f"\n📊 Total documents loaded: {len(documents)}")


# Split text into chunks
print("✂️ Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Embed using HuggingFace
print("🔗 Generating embeddings using HuggingFace model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create and save FAISS vector DB
print("\n💾 Creating FAISS vector store...\n")

vectors = []
docs = []

for i, doc in enumerate(texts):
    print(f"➡️ Processing document {i + 1} of {len(texts)}: {doc.metadata.get('source', 'Unknown')}")

    # Embed and show quick confirmation
    embedding = embeddings.embed_query(doc.page_content)
    print("   ✅ Embedded")

    vectors.append(embedding)
    docs.append(doc)

    print("   ✅ Added to list\n")

# Now create FAISS vector store
print("⚙️ Building FAISS index...")
db = FAISS.from_documents(docs, embeddings)

print("💾 Saving FAISS index locally...")
db.save_local(db_dir)

print(f"✅ Vector database created and saved to: {db_dir}")
