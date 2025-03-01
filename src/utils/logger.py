import logging
import os
from datetime import datetime


Log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")

os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, Log_file)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(filename)s - %(lineno)d - %(levelname)s - %(message)s"

)

logger = logging.getLogger(__name__)