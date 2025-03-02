from src.utils.exception import FacebookBotException
from src.utils.logger import logger
from src.config.config import FACEBOOK_ACCESS_TOKEN
import requests
import sys

def reply_to_comment(comment_id, message):
    """Replies to a Facebook comment"""

    url = f"https://graph.facebook.com/v21.0/{comment_id}/comments"
    params = {
        "message": message,
        "access_token": FACEBOOK_ACCESS_TOKEN
    }

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        logger.info(f"Replied to comment {comment_id}: {message}")
    except Exception as e:
        logger.error(f"Error replying to comment {comment_id}: {e}")
        raise FacebookBotException(e, sys)
    
