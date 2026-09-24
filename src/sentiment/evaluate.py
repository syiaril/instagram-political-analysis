import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import json
import os
from src.sentiment.analyzer import predict

def evaluate_model():
    validation_file = os.path.join("data", "validation", "sentiment_validation.csv")
    
    if not os.path.exists(validation_file):
        print(f"Validation file {validation_file} not found.")
        return
        
    print(f"Loading validation dataset from {validation_file}...")
    df = pd.read_csv(validation_file)
    
    if 'actual_sentiment' not in df.columns or 'comment_text' not in df.columns:
        print("Dataset must contain 'comment_text' and 'actual_sentiment' columns.")
        return
        
    print("Running model predictions...")
    # Predict sentiment using our current model
    predictions = df['comment_text'].apply(lambda x: predict(str(x))['sentiment'])
    
    # Calculate metrics
    y_true = df['actual_sentiment']
    y_pred = predictions
    
    # We specify labels to ensure correct order in confusion matrix and metrics
    labels = ["positive", "neutral", "negative"]
    
    acc = accuracy_score(y_true, y_pred)
    # Using weighted average for multiclass precision/recall/f1
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    results = {
        "accuracy": round(acc, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4),
        "confusion_matrix": {
            "labels": labels,
            "matrix": cm.tolist()
        }
    }
    
    print("\n--- Evaluation Results ---")
    print(json.dumps(results, indent=4))
    
if __name__ == "__main__":
    evaluate_model()
