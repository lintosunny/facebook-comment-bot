from src.utils.exception import FacebookBotException
from src.utils.logger import logger
from src.utils.helpers import load_prompt
from src.config.config import GEMINI_API_KEY
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

def generate_ai_response(comment: str) -> str:
    """Return AI generated reply for comments"""  
    try:
        prompt_temp = load_prompt()
        prompt = f"{prompt_temp} \n comment to respond to: {comment}. \n return only the reply without any extra text."
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        logger.info(f"reply generated for '{comment}': '{response.text}'")
        return response.text
    
    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        raise FacebookBotException("Failed to generate AI response")