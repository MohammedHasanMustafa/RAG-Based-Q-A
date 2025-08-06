import pandas as pd

# Load the full dataset
df = pd.read_csv("data/labeled_newscatcher_dataset.csv", sep=";", encoding="utf-8")

# Normalize the topic column to lowercase and strip spaces
df['topic'] = df['topic'].str.strip().str.lower()

# Filter for technology articles
tech_df = df[df['topic'] == 'technology']

# Show the top rows
print(tech_df.head())
print(f"\nTotal technology articles: {len(tech_df)}")

# Optionally, save to new CSV
tech_df.to_csv("data/technology_articles.csv", index=False)
