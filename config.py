import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
print("🔄 Loading environment variables from .env...")
load_dotenv()

# Get the Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("🔍 GEMINI_API_KEY found." if GEMINI_API_KEY else "❌ GEMINI_API_KEY not found!")

# Check if key is set
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

# Initialize the LLM
print("🚀 Initializing Gemini LLM...")
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0,
    google_api_key=GEMINI_API_KEY
)
print("✅ Gemini LLM initialized successfully.")
