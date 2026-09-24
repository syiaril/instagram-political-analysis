import re

def clean_text(text: str, remove_urls=True, remove_mentions=True, remove_hashtags=False, remove_emojis=False, normalize_repeated=True) -> str:
    if not isinstance(text, str):
        return ""
        
    cleaned = text
    
    if remove_urls:
        cleaned = re.sub(r'http\S+|www\S+|https\S+', '', cleaned, flags=re.MULTILINE)
        
    if remove_mentions:
        cleaned = re.sub(r'@\w+', '', cleaned)
        
    if remove_hashtags:
        cleaned = re.sub(r'#\w+', '', cleaned)
        
    if remove_emojis:
        # Basic regex for emojis (can be improved with specialized emoji library if needed)
        cleaned = re.sub(r'[^\w\s,\.\!\?]', '', cleaned)
        
    if normalize_repeated:
        # Reduce repeated characters to max 2 (e.g., "goblokkk" -> "goblokk", "😡😡😡" -> "😡😡")
        cleaned = re.sub(r'(.)\1{2,}', r'\1\1', cleaned)
        
    # Remove extra whitespaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned
