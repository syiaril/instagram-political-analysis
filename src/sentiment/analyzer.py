import os
import json
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# Optional: Set your GEMINI_API_KEY as an environment variable in Colab
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"

# Ensure the client is initialized (it will automatically look for GEMINI_API_KEY in the environment)
try:
    client = genai.Client()
except Exception as e:
    client = None

# Define the structured output format
class SentimentResult(BaseModel):
    sentiment: str = Field(description="The sentiment of the comment: 'negative', 'neutral', or 'positive'")
    confidence: float = Field(description="Confidence score between 0.0 and 1.0")

def predict(text: str) -> dict:
    """
    Real sentiment prediction using Gemini API.
    """
    if not client:
        # Fallback if API Key is not set
        return {"sentiment": "neutral", "confidence": 0.0}

    prompt = f"""
    Tugas Anda adalah melakukan analisis sentimen politik pada komentar Instagram masyarakat Indonesia berikut.
    Banyak komentar yang menggunakan bahasa slang, sarkasme, atau singkatan. 
    Klasifikasikan sentimennya terhadap pemerintah/kebijakan menjadi: 'negative', 'neutral', atau 'positive'.
    
    Berikan output dalam format JSON strict (tanpa blok markdown) dengan keys:
    - "sentiment": ("negative", "neutral", "positive")
    - "confidence": (float antara 0.0 sampai 1.0)
    
    Komentar: "{text}"
    """
    
    try:
        interaction = client.interactions.create(
            model='gemini-3.7-flash',
            input=prompt,
        )
        
        # Clean markdown codeblocks if model returns it
        out_text = interaction.output_text.strip()
        if out_text.startswith("```json"):
            out_text = out_text[7:]
        if out_text.endswith("```"):
            out_text = out_text[:-3]
            
        result = json.loads(out_text.strip())
        return {
            "sentiment": result.get("sentiment", "neutral").lower(),
            "confidence": result.get("confidence", 0.0)
        }
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return {"sentiment": "neutral", "confidence": 0.0}
