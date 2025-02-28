import google.generativeai as genai
from src.config import GEMINI_API_KEY
from src.utils.logger import logger
from src.utils.exceptions import GeminiAPIError

genai.configure(api_key=GEMINI_API_KEY)

def generate_ai_response(comment: str) -> str:
    
    prompt = f"reply to this {comment}"

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        raise GeminiAPIError("Failed to generate AI response")