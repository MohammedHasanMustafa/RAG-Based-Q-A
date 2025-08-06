import os
import pandas as pd
import logging
from newspaper import Article
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Paths
INPUT_CSV = "data/technology_articles.csv"
EXTRACTED_DIR = "data/extracted_articles"
FAILED_CSV = "data/failed_urls.csv"
MAX_WORKERS = 20  # Increase to 20 if internet is fast/stable

# Prepare folders
os.makedirs(EXTRACTED_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(filename='data/article_errors.log', level=logging.ERROR)

# Read CSV and deduplicate
df = pd.read_csv(INPUT_CSV)
df = df.drop_duplicates(subset="link").reset_index(drop=True)

# Track already processed
existing_files = set(os.listdir(EXTRACTED_DIR))
processed_indices = {int(f.replace("article", "").replace(".txt", "")) for f in existing_files if f.startswith("article")}

# Result containers
failed_articles = []
success_count = 0

def fetch_and_save(idx, row):
    article_number = idx + 1
    if article_number in processed_indices:
        return None  # Skip

    url = row["link"]
    title = row["title"]
    filename = os.path.join(EXTRACTED_DIR, f"article{article_number}.txt")

    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text.strip()
        if not text:
            raise ValueError("Empty article")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{text}")

        return ("success", article_number)
    except Exception as e:
        logging.error(f"Article {article_number} failed - {url}\nReason: {str(e)}\n")
        return ("fail", article_number, url)

# Run in parallel
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(fetch_and_save, idx, row): idx for idx, row in df.iterrows()}

    for future in tqdm(as_completed(futures), total=len(futures), desc="Extracting Articles"):
        result = future.result()
        if result:
            if result[0] == "success":
                success_count += 1
            elif result[0] == "fail":
                _, article_number, url = result
                failed_articles.append({"article_number": article_number, "url": url})

# Save failed URLs
if failed_articles:
    failed_df = pd.DataFrame(failed_articles)
    failed_df.to_csv(FAILED_CSV, index=False)

# Summary
print("\nExtraction Summary:")
print(f"✅ Successfully extracted: {success_count}")
print(f"❌ Failed to extract: {len(failed_articles)}")
print(f"📝 Extracted articles saved to: {EXTRACTED_DIR}")
if failed_articles:
    print(f"📄 Failed URLs saved to: {FAILED_CSV}")
