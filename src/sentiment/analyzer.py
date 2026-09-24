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
    
    Komentar: "{text}"
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=SentimentResult,
                temperature=0.1,
            ),
        )
        
        # Parse the JSON response
        result = json.loads(response.text)
        return {
            "sentiment": result.get("sentiment", "neutral").lower(),
            "confidence": result.get("confidence", 0.0)
        }
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return {"sentiment": "neutral", "confidence": 0.0}
