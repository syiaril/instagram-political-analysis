# TODO: Later replace with a real model pipeline loading from HuggingFace
MODEL_NAME = "mock-indonesian-sentiment"

def predict(text: str) -> dict:
    """
    Mock sentiment prediction.
    In real implementation, this will use the Transformers model.
    """
    # Simple mock logic for demonstration
    text_lower = text.lower()
    
    if "buruk" in text_lower or "ecewa" in text_lower or "gagal" in text_lower or "becus" in text_lower:
        return {"sentiment": "negative", "confidence": 0.94}
        
    if "hebat" in text_lower or "bagus" in text_lower:
        # Could be positive or sarcasm, mock as positive for now
        return {"sentiment": "positive", "confidence": 0.85}
        
    return {"sentiment": "neutral", "confidence": 0.70}
