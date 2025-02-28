import requests
from src.config import FACEBOOK_ACCESS_TOKEN, PAGE_ID
from src.utils.logger import logger
from src.utils.exceptions import FacebookAPIError

def get_comments_from_posts():
    """Fetches latest comments from Facebook posts."""
    url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/feed?fields=id,comments"
    params = {"access_token": FACEBOOK_ACCESS_TOKEN}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        comments = []
        for post in data.get('data', []):
            if 'comments' in post and 'data' in post['comments']:
                for comment in post['comments']['data']:
                    comments.append({
                        "id": comment.get("id"),
                        "message": comment.get("message")
                    })
        return comments

    except requests.exceptions.RequestException as e:
        logger.error(f"Facebook API error: {e}")
        raise FacebookAPIError("Failed to fetch comments")

def reply_to_comment(comment_id, message):
    """Replies to a Facebook comment."""
    url = f"https://graph.facebook.com/v21.0/{comment_id}/comments"
    params = {
        "message": message,
        "access_token": FACEBOOK_ACCESS_TOKEN
    }

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        logger.info(f"Replied to comment {comment_id}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error replying to comment {comment_id}: {e}")
        raise FacebookAPIError("Failed to reply to comment")
