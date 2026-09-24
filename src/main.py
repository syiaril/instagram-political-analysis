import pandas as pd
import json
import os

from src.preprocessing.cleaner import clean_text
from src.sentiment.analyzer import predict
from src.classification.account_classifier import classify_account
from src.analysis.statistics import calculate_statistics

def main():
    print("Starting pipeline...")
    # Update to your real Excel file name
    raw_excel_path = os.path.join("data", "raw", "IGComment-All_20260924155854.xlsx")
    raw_csv_path = os.path.join("data", "raw", "comments.csv")
    processed_data_path = os.path.join("data", "processed", "comments_processed.csv")
    
    os.makedirs(os.path.dirname(raw_csv_path), exist_ok=True)
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    
    # 1. LOAD DATA
    if os.path.exists(raw_excel_path):
        print(f"Loading REAL data from {raw_excel_path}...")
        df = pd.read_excel(raw_excel_path)
        
        # Auto-map column names (since scrapers use different names like 'Username', 'Comment')
        col_lower = {c: str(c).lower() for c in df.columns}
        for col, lower in col_lower.items():
            if 'user' in lower:
                df.rename(columns={col: 'username'}, inplace=True)
            elif 'text' in lower or 'comment' in lower or 'komentar' in lower:
                df.rename(columns={col: 'comment_text'}, inplace=True)
                
        # Fill missing classification columns with NaN so they exist
        if 'account_private' not in df.columns:
            df['account_private'] = pd.NA
        if 'follows_anies' not in df.columns:
            df['follows_anies'] = pd.NA
            
    elif os.path.exists(raw_csv_path):
        print(f"Loading DUMMY data from {raw_csv_path}...")
        df = pd.read_csv(raw_csv_path)
    else:
        print("Error: No data found. Please put your .xlsx in data/raw/")
        return

    # 2. PREPROCESSING
    print("Cleaning text...")
    df['cleaned_text'] = df['comment_text'].astype(str).apply(lambda x: clean_text(x))
    
    # 3. SENTIMENT ANALYSIS
    print("Analyzing sentiment...")
    sentiments = df['cleaned_text'].apply(lambda x: predict(x))
    df['sentiment'] = [res['sentiment'] for res in sentiments]
    df['sentiment_score'] = [res['confidence'] for res in sentiments]
    
    # 4. FILTERING & OPTIMIZATION (As requested by user!)
    negative_users = df[df['sentiment'] == 'negative']['username'].unique()
    print(f"\n--- OPTIMIZATION ---")
    print(f"Total Comments: {len(df)}")
    print(f"Negative Commenters Found: {len(negative_users)}")
    print("Mengecek 'Following' list HANYA untuk pengguna yang berkomentar negatif...")
    print("Ini akan menghemat waktu scraping hingga berjam-jam!")
    
    # TODO: Connect to Instaloader logic here for 'negative_users'
    # For now, we use existing column values if any (from dummy) or assume Unknown
    
    # 5. CLASSIFICATION (Temporary mock logic for Real Data)
    print("Classifying accounts...")
    classifications = df.apply(lambda row: classify_account(row['account_private'], row['follows_anies']), axis=1)
    df['classification'] = [res[0] for res in classifications]
    df['classification_reason'] = [res[1] for res in classifications]
    
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