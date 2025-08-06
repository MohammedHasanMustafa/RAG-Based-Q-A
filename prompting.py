from config import llm  # Import the initialized Gemini LLM from config.py

# ✨ Prompt template builder
def build_prompt(article_text: str) -> str:
    """
    Builds a prompt for summarizing an article in 3 bullet points.
    """
    print("🧠 Building prompt...")
    prompt = f"""
You are a skilled tech journalist. Summarize the following article in **exactly 3 bullet points**:

\"\"\"
{article_text}
\"\"\"

Make the bullet points informative, concise, and insightful.
"""
    print("✅ Prompt built successfully!\n")
    return prompt

# 🚀 Function to generate completion from Gemini
def generate_summary(article_text: str) -> str:
    """
    Generates a summary using Gemini for a given article.
    """
    print("🛠️ Preparing to generate summary...")
    prompt = build_prompt(article_text)

    print("📨 Sending prompt to Gemini LLM...\n")
    print("🔍 Prompt Preview:")
    print("-" * 60)
    print(prompt.strip())
    print("-" * 60)

    try:
        response = llm.invoke(prompt)
        print("\n✅ Response received from Gemini!\n")
        print("📌 Summary Output:")
        print("-" * 60)
        print(response.content.strip())
        print("-" * 60)
        return response.content.strip()
    except Exception as e:
        print("❌ An error occurred during generation:")
        print(e)
        return f"❌ Error during completion: {e}"

# 🧪 Test the prompt
if __name__ == "__main__":
    sample_text = """
    Google has announced the release of Gemini 2.0, its most powerful AI model yet.
    This release includes a lightweight version called Gemini 2.0 Flash, optimized for fast responses.
    The company also shared plans to integrate Gemini across Workspace, Search, and Android.
    """

    print("📄 Original Article:")
    print("-" * 60)
    print(sample_text.strip())
    print("-" * 60)

    print("\n📢 Generating summary...\n")
    summary = generate_summary(sample_text)

    print("\n🎯 Final Summary:")
    print(summary)
