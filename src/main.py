import pandas as pd
import json
import os

from src.preprocessing.cleaner import clean_text
from src.sentiment.analyzer import predict
from src.classification.account_classifier import classify_account
from src.analysis.statistics import calculate_statistics

def main():
    print("Starting pipeline...")
    raw_data_path = os.path.join("data", "raw", "comments.csv")
    processed_data_path = os.path.join("data", "processed", "comments_processed.csv")
    
    if not os.path.exists(raw_data_path):
        print(f"Error: Raw data file {raw_data_path} not found.")
        return

    # Load raw data
    print(f"Loading data from {raw_data_path}...")
    df = pd.read_csv(raw_data_path)
    
    # Preprocessing
    print("Cleaning text...")
    df['cleaned_text'] = df['comment_text'].apply(lambda x: clean_text(x))
    
    # Sentiment Analysis
    print("Analyzing sentiment...")
    sentiments = df['cleaned_text'].apply(lambda x: predict(x))
    df['sentiment'] = [res['sentiment'] for res in sentiments]
    df['sentiment_score'] = [res['confidence'] for res in sentiments]
    
    # Account Classification
    print("Classifying accounts...")
    classifications = df.apply(lambda row: classify_account(row['account_private'], row['follows_anies']), axis=1)
    df['classification'] = [res[0] for res in classifications]
    df['classification_reason'] = [res[1] for res in classifications]
    
    print("\n--- DEBUG INFO ---")
    for idx, row in df.iterrows():
        print(f"Row {idx}: {row['username']} | text: {row['cleaned_text']} | sentiment: {row['sentiment']} | follows: {row['follows_anies']} -> class: {row['classification']}")
    print("------------------\n")
    
    # Save processed data
    print(f"Saving processed data to {processed_data_path}...")
    df.to_csv(processed_data_path, index=False)
    
    # Aggregation & Statistics
    print("Calculating statistics...")
    stats = calculate_statistics(df)
    
    print("\n--- Pipeline Completed ---")
    print(json.dumps(stats, indent=4))


if __name__ == "__main__":
    main()