import os 
from dotenv import load_dotenv

load_dotenv()

FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')