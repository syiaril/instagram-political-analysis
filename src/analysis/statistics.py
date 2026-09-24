import pandas as pd

def calculate_statistics(df: pd.DataFrame) -> dict:
    """
    Calculates aggregation statistics from the processed DataFrame.
    """
    if df.empty:
        return {
            "total_negative": 0,
            "anies": {"count": 0, "percentage": 0.0},
            "neutral": {"count": 0, "percentage": 0.0},
            "private": {"count": 0, "percentage": 0.0}
        }
        
    # Filter only negative comments (if the df contains others)
    df_negative = df[df['sentiment'] == 'negative']
    total_negative = len(df_negative)
    
    if total_negative == 0:
        return {
            "total_negative": 0,
            "anies": {"count": 0, "percentage": 0.0},
            "neutral": {"count": 0, "percentage": 0.0},
            "private": {"count": 0, "percentage": 0.0}
        }
        
    counts = df_negative['classification'].value_counts()
    
    anies_count = int(counts.get('ANIES', 0))
    neutral_count = int(counts.get('NEUTRAL', 0))
    private_count = int(counts.get('PRIVATE', 0))
    
    return {
        "total_negative": total_negative,
        "anies": {
            "count": anies_count,
            "percentage": round((anies_count / total_negative) * 100, 2)
        },
        "neutral": {
            "count": neutral_count,
            "percentage": round((neutral_count / total_negative) * 100, 2)
        },
        "private": {
            "count": private_count,
            "percentage": round((private_count / total_negative) * 100, 2)
        }
    }
