# Implementation Plan: Instagram Political Comment Analysis (Revised)

## Directory Structure
```
instagram-political-analysis/
│
├── data/
│   ├── raw/
│   │   └── comments.csv
│   │
│   ├── processed/
│   │   └── comments_processed.csv
│   │
│   └── validation/
│       └── sentiment_validation.csv
│
├── src/
│   ├── collector/
│   │   ├── __init__.py
│   │   └── instagram.py
│   │
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   └── cleaner.py
│   │
│   ├── sentiment/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   └── evaluate.py
│   │
│   ├── classification/
│   │   ├── __init__.py
│   │   └── account_classifier.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   └── main.py
│
├── tests/
│
├── dashboard.py
├── requirements.txt
├── PROJECT.md
└── README.md
```

## Step 1 — Environment
* Use **Python 3.13** (to ensure ecosystem compatibility for PyTorch/Transformers/Pandas).
* Dependencies:
  - `pandas`
  - `transformers`
  - `torch`
  - `scikit-learn` (for model evaluation metrics)
  - `plotly`
  - `streamlit`

## Step 2 — Data Schema
**Raw Data Schema:**
- `post_id`
- `post_url`
- `comment_id`
- `username`
- `comment_text`
- `timestamp`
- `account_private`
- `follows_anies`

**Processed Data Schema:**
- `post_id`
- `comment_id`
- `comment_text`
- `cleaned_text`
- `sentiment`
- `sentiment_score`
- `account_private`
- `follows_anies`
- `classification`

## Step 3 — Cleaning
Implement `clean_text(text, **kwargs)` with configurable flags:
- `remove_urls = True`
- `remove_mentions = True`
- `remove_hashtags = False`
- `remove_emojis = False` (Keep emojis as they provide sentiment context)
- `normalize_repeated = True`

## Step 4 — Sentiment
Create an interface for the analyzer:
```python
def predict(text):
    return {
        "sentiment": "negative",
        "confidence": 0.94
    }
```
Isolate the `MODEL_NAME` to easily swap out models if initial performance is poor.

## Step 5 — Classification
Implement `classify_account(is_private, follows_anies)`:
* Include the reasoning in the output:
  - `classification = ANIES`, `classification_reason = follows_anies`
  - `classification = PRIVATE`, `classification_reason = account_private`

## Step 6 — Aggregation
Implement `calculate_statistics(df)` to precompute dashboard metrics (total counts and percentages for Anies, Neutral, and Private).

## Step 7 — Evaluation
Test the model against a manual dataset of 500 comments (positive/neutral/negative) to calculate:
- Accuracy, Precision, Recall, and F1-Score.

## Step 8 — Instagram Collector
Design an interface first:
```python
class InstagramCollector:
    def get_posts(self): pass
    def get_comments(self, post_id): pass
    def get_account_info(self, username): pass
```
Allows swapping backend (API, scraper, dataset) without breaking downstream.

## Step 9 — Dashboard
Use Streamlit and Plotly to display overall metrics, negative comment composition (Pie Chart), and filters.

## Step 10 — Final Architecture
Instagram -> Collector -> Raw Dataset -> Cleaner -> Sentiment Model -> Negative Filter -> Account Classification -> Statistics -> Dashboard.
