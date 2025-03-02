from src.models.auto_comment import auto_reply_to_comments
from src.utils.helpers import logger
from src.utils.helpers import FacebookBotException
import sys

def main():
    """Main function to run facebook comment bot"""

    try:
        logger.info("Starting the facebook comment bot...")
        auto_reply_to_comments()
        logger.info("Facebook comment bot finished sucessfully.")
    
    except Exception as e:
        logger.critical(f"Critical error in the bot: {e}", exc_info=True)
        sys.exit(1)  # Exit with error code


if __name__ == "__main__":
    main()
