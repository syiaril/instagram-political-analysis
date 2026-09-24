from transformers import pipeline


def create_sentiment_analyzer():
    return pipeline(
        "sentiment-analysis",
        model="w11wo/indonesian-roberta-base-sentiment-classifier"
    )


def analyze_sentiment(analyzer, text):
    result = analyzer(text)[0]

    label = result["label"].lower()
    score = result["score"]

    return label, score