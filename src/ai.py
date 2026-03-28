from google import genai
from src.settings import GEMINI_API_KEY
import json

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_ai_batch(pages_dict):
    if not pages_dict:
        return {}

    prompt = """
    Extract lead information from the following list of web pages.
    Find the person's name, company, email, and phone number.
    Clean up all whitespace in the values. Use empty strings if a value is not found.
    Output ONLY a raw JSON array of objects. Each object MUST have the exact keys: "url", "name", "company", "email", "phone".
    DO NOT wrap the output in markdown code blocks like ```json.
    
    PAGES:
    """

    for url, text in pages_dict.items():
        prompt += f"\n--- URL: {url} ---\nTEXT:\n{text[:3000]}\n"

    try:
        res = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Clean up common AI markdown formatting
        text_res = res.text.strip()
        if text_res.startswith("```json"):
            text_res = text_res[7:-3].strip()
        elif text_res.startswith("```"):
            text_res = text_res[3:-3].strip()
            
        json_array = json.loads(text_res)
        
        # Convert array of dicts to a map of {url: result} for easy lookup
        return {item.get("url", ""): item for item in json_array if isinstance(item, dict)}
        
    except Exception as e:
        print(f"AI Batch Parse Error: {e}")
        return {}