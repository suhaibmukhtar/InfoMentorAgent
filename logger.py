import logging
import os
from config import Log_dir
from datetime import datetime


LOG_DIR = Log_dir
os.makedirs(Log_dir, exist_ok=True)

LOG_FILE_NAME = f"Logs{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE_NAME)),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    logging.info("Logger is working")



