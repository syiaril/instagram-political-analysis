import sys
sys.path.append('.')
from src.preprocessing.cleaner import clean_text
from src.sentiment.analyzer import predict
import pandas as pd

df = pd.read_csv('data/raw/comments.csv')
for i, row in df.iterrows():
    text = row['comment_text']
    cleaned = clean_text(text)
    pred = predict(cleaned)
    if pred['sentiment'] == 'negative':
        print(f"Row {i} is NEGATIVE: {text}")
        print(f"follows_anies={row['follows_anies']} type={type(row['follows_anies'])}")
