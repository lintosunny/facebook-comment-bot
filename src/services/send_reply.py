
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
    
