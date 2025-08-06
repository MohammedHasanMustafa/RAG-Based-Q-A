import os
import pandas as pd
import re

# 📁 Path to folder with extracted articles
articles_dir = "data/extracted_articles"

# ✅ Classifier function using \b for whole-word matching
def classify_tech_article(text):
    text_lower = text.lower()

    def keyword_found(keywords):
        pattern = r"\b(" + "|".join(re.escape(kw) for kw in keywords) + r")\b"
        return re.search(pattern, text_lower) is not None

    ai_keywords = [
        "ai", "artificial intelligence", "machine learning", "neural", "deep learning",
        "chatgpt", "gpt", "llm", "natural language processing", "nlp", "vision model",
        "generative ai", "openai", "voice assistant", "chatbot"
    ]

    cloud_keywords = [
        "cloud", "aws", "azure", "gcp", "google cloud", "cloud computing", "remote server",
        "kubernetes", "docker", "devops", "virtual machine", "cloud storage",
        "saas", "paas", "iaas", "serverless"
    ]

    mobile_keywords = [
        "android", "ios", "smartphone", "mobile", "iphone", "ipad", "tablet",
        "galaxy", "samsung", "pixel", "oneplus", "smartwatch", "wearable",
        "earbuds", "fold", "flip", "z fold", "buds", "headphones", "macbook", "battery"
    ]

    gaming_keywords = [
        "game", "gaming", "xbox", "playstation", "ps5", "nintendo", "esports",
        "pc game", "console", "steam", "epic games", "controller", "gamer", "funko pop"
    ]

    cybersecurity_keywords = [
        "security", "malware", "hacker", "cyber", "phishing", "breach",
        "firewall", "ransomware", "encryption", "zero-day", "ddos", "2fa", "cyberattack"
    ]

    social_keywords = [
        "tiktok", "facebook", "instagram", "snapchat", "twitter", "x.com", "youtube",
        "social media", "tweet", "reels", "shorts", "threads", "elon musk"
    ]

    if keyword_found(ai_keywords):
        return "AI"
    elif keyword_found(cloud_keywords):
        return "Cloud"
    elif keyword_found(mobile_keywords):
        return "Mobile"
    elif keyword_found(gaming_keywords):
        return "Gaming"
    elif keyword_found(cybersecurity_keywords):
        return "Cybersecurity"
    elif keyword_found(social_keywords):
        return "Social Media"
    else:
        return "Other"


# 🧠 Collect metadata
metadata = []

print(f"📂 Scanning folder: {articles_dir}\n")

for filename in sorted(os.listdir(articles_dir)):
    if filename.endswith(".txt"):
        filepath = os.path.join(articles_dir, filename)
        print(f"🔍 Reading: {filename}")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            label = classify_tech_article(text)
            print(f"   🏷️ Category: {label}")
            metadata.append({
                "article_file": filename,
                "category": label
            })
        except Exception as e:
            print(f"   ❌ Error reading file: {e}")
    else:
        print(f"⏭️ Skipping non-txt file: {filename}")

# 📝 Save metadata to CSV
metadata_df = pd.DataFrame(metadata)
output_path = "data/metadata.csv"
metadata_df.to_csv(output_path, index=False)

print("\n✅ Classification Complete!")
print(f"📄 Metadata saved to: {output_path}")
print(f"🧾 Total articles processed: {len(metadata)}")
