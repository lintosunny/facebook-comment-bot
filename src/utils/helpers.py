from src.utils.exception import FacebookBotException
from src.utils.logger import logger
from datetime import datetime
import requests
import sys
import os
import json


artifact_file = "last_updated.json"
artifact_path = os.path.join(os.getcwd(), "artifacts")
ARTIFACT_FILEPATH = os.path.join(artifact_path, artifact_file)


def str_to_date(fb_date: str) -> datetime:
    try:
        converted_date = datetime.strptime(fb_date, "%Y-%m-%dT%H:%M:%S%z")
        logger.info(f"{fb_date} converted to datetime")
        return converted_date
    except Exception as e:
        logger.info(f"{fb_date} not converted to datetime")
        raise FacebookBotException (e, sys)
    
    
def date_to_str(date_inp: datetime) -> str:
    try:
        converted_date = date_inp.strftime("%Y-%m-%dT%H:%M:%S%z")
        logger.info(f"{date_inp} converted to str")
        return converted_date
    except Exception as e:
        logger.info(f"{date_inp} not converted to str")
        raise FacebookBotException (e, sys)


def get_last_updated():
    default_datetime = datetime.min # Returns 0001-01-01
    
    if not os.path.exists(ARTIFACT_FILEPATH):
        os.makedirs(artifact_path, exist_ok=True)
        logger.info("Artifact path created")

        data = {"last_updated_str":date_to_str(default_datetime)}
        with open(ARTIFACT_FILEPATH, "w") as file:
            json.dump(data, file)
        logger.info(f"json file created at {ARTIFACT_FILEPATH} and updated last_updated")
        
        logger.info("no last_updated.json found, returning default date.")
        return default_datetime 
    
    with open(ARTIFACT_FILEPATH, "r+") as file:
        if os.path.getsize(ARTIFACT_FILEPATH) == 0:
            json.dump({"last_updated_str":date_to_str(default_datetime)}, file)
            logger.info(f"updated last_updated.json to {default_datetime}")
        
            logger.info("no last_updated.json found, returning default date.")
            return default_datetime
        
        try:
            data = json.load(file)
            last_updated = str_to_date(data["last_updated_str"])
            logger.info("loaded last updated date")
            return last_updated
        except Exception as e:
            logger.info(f"Didn't get last updated date")
            raise FacebookBotException (e, sys)
        

def update_last_updated(new_time):
    try:
        with open(ARTIFACT_FILEPATH, "w") as file:
            json.dump({"last_updated_str":date_to_str(new_time)}, file)
        logger.info(f"updated last_updated.json to {new_time}")
    except Exception as e:
            logger.info(f"Didn't update last_updated.json")
            raise FacebookBotException (e, sys)
    
'''
if __name__ == "__main__":
    try:
        update_last_updated(datetime.now())


    except Exception as e:
        raise FacebookBotException(e, sys)

'''