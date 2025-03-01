from src.services.get_comment import get_comments_from_posts, reply_to_comment
from src.services.ai_reply import generate_ai_response
from src.utils.logger import logger

def process_comments():
    """Fetches comments and replies using AI."""
    comments = get_comments_from_posts()
    for comment in comments:
        comment_id = comment["id"]
        message = comment["message"]

        # Generate AI response
        ai_response = generate_ai_response(message)

        # Reply to the comment
        reply_to_comment(comment_id, ai_response)
        logger.info(f"Replied to comment {comment_id} with message: {ai_response}")

if __name__ == "__main__":
    process_comments()