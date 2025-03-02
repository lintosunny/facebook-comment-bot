from src.utils.exception import FacebookBotException
from src.utils.logger import logger
from src.config import GEMINI_API_KEY
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

def generate_ai_response(comment: str) -> str:
    """Return AI generated reply for comments"""  

    prompt = f"""
    Generate concise, engaging, and relevant replies to Facebook comments on Playful Pick’s posts. Responses should be minimal yet meaningful, using emojis where appropriate to enhance engagement. The AI should only reply to comments directly related to the post or the company’s products and services.
    
    Responses should be 1 friendly, and clear. If the comment contains a question about plushy toys, product details, pricing, shipping, or parenting-related discussions, the AI should provide a direct and helpful answer. If emojis add to the tone, use them sparingly and effectively.
    
    Do not generate responses to 18+ or illegal topics.
    If a comment is unrelated to the post or company, the AI should reply with: "Please contact support@playfulpicks.com for support."
    Ensure accuracy when mentioning product details, pricing, or promotions. Avoid making up product information.
    Maintain a warm, playful, and professional tone that aligns with Playful Pick’s branding.
    
    Playful Pick is an online toy store specializing in plushy toys that bring joy to children and support parents. The brand focuses on fostering a magical playtime experience while creating a supportive community for moms.
    Posts highlight adorable plush toy collections, parenting support, exclusive offers, and giveaways.
    Products are priced at $4.99 each, with free shipping.
    Products available at playfulpicks.com
    The audience includes parents, gift shoppers, and plush toy enthusiasts.
    Responses should reflect Playful Pick’s friendly and engaging voice, keeping interactions delightful and brand-aligned.

    comment to respond to: {comment}

    return only the reply without any extra text.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        logger.info(f"reply generated for '{comment}': '{response.text}'")
        return response.text
    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        raise FacebookBotException("Failed to generate AI response")
