from src.utils.exception import FacebookBotException
from src. utils.logger import logger
from src.utils.helpers import update_last_updated
from src.services.ai_reply import generate_ai_response
from src.services.get_comment import get_comment
from src.services.send_reply import reply_to_comment
import sys

def auto_reply_to_comments():
    """Fetches comments and replies using AI"""

    try:
        comments = get_comment()
        for comment in comments:
            comment_id = comment["id"]
            message = comment["message"]

            if not comment_id or not message:
                logger.warning("Skipping comment due to missing id or message")
                continue
            
            try:
                # Generate AI response
                ai_response = generate_ai_response(message)

                # Reply to the comment
                reply_to_comment(comment_id, ai_response)
                logger.info(f"Replied to comment {comment_id} with message: {ai_response}")

            except Exception as e:
                logger.error(f"Error processing comment {comment_id}: {e}")
                raise FacebookBotException(e, sys)
            
        update_last_updated()
        logger.info("last_updated is updated")

    except Exception as e:
        logger.critical(f"Critical error in auto_reply_comments: {e}", exc_info=True)
        raise FacebookBotException(e, sys)
    

if __name__ == "__main__":
    auto_reply_to_comments()