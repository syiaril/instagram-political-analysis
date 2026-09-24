import pandas as pd

from sentiment import create_sentiment_analyzer, analyze_sentiment
from classifier import classify_account


INPUT_FILE = "data/raw_comments.csv"
OUTPUT_FILE = "data/processed_comments.csv"


def main():
    print("Membaca data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Total komentar: {len(df)}")

    print("\nMemuat model sentiment analysis...")
    analyzer = create_sentiment_analyzer()

    sentiments = []

    print("\nMenganalisis komentar...")

    for _, row in df.iterrows():
        label, score = analyze_sentiment(
            analyzer,
            row["comment_text"]
        )

        sentiments.append({
            "sentiment": label,
            "sentiment_score": score
        })

    sentiment_df = pd.DataFrame(sentiments)

    df = pd.concat(
        [df.reset_index(drop=True), sentiment_df],
        axis=1
    )

    # Hanya komentar negatif
    negative_df = df[
        df["sentiment"].str.lower() == "negative"
    ].copy()

    print(f"\nKomentar negatif: {len(negative_df)}")

    # Klasifikasi akun
    negative_df["classification"] = negative_df.apply(
        lambda row: classify_account(
            row["account_private"],
            row["follows_anies"]
        ),
        axis=1
    )

    # Hitung jumlah
    counts = negative_df["classification"].value_counts()

    total = len(negative_df)

    print("\n=== HASIL ANALISIS ===")

    for category in ["anies", "neutral", "private"]:
        count = counts.get(category, 0)

        percentage = (
            count / total * 100
            if total > 0
            else 0
        )

        print(
            f"{category.upper():8} : "
            f"{count:4} akun "
            f"({percentage:.2f}%)"
        )

    negative_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"\nData disimpan ke: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()