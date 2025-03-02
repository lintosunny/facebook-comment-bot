from src.utils.exception import FacebookBotException
from src.utils.logger import logger
from src.config import FACEBOOK_ACCESS_TOKEN
from src.config import PAGE_ID
from src.utils.helpers import str_to_date
from src.utils.helpers import get_last_updated
import requests
import logging
import os, requests
import sys

page_id = PAGE_ID
token = FACEBOOK_ACCESS_TOKEN
last_updated_date = get_last_updated()


def get_comment():
    """Fetches comments from a Facebook page feed using Graph API."""
    try:
        if not page_id or not token:
            logger.error('missing PAGE_ID or FACEBOOK_ACCESS_TOKEN in the env variables')
            return []
        
        url = f"https://graph.facebook.com/v21.0/{page_id}/feed"
        params = {
             "access_token": token,
            "fields":'comments'
         }

        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        comments_list = []

        for item in data.get('data', []):
            if 'comments' in item and 'data' in item['comments']:
                for comment in item['comments']['data']:
                    try:
                        if (str_to_date(comment['created_time']) > last_updated_date) and (comment['from']['id'] != page_id):               
                            comments_list.append({"id": comment['id'], "message": comment['message']})
                            logger.info(f"{comment['id']} added to comments_list")
                    except Exception as e:
                        logger.info(f"skipping {comment['id']} due to {e}")
                        raise FacebookBotException (e, sys)

        logger.info(f"succesfully fetched {len(comments_list)} comments.")
        return comments_list
    
    except Exception as e:
        logger.error(f"failed due to {e}")
        raise FacebookBotException (e, sys)