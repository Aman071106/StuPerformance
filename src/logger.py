"""Custom logger configuration file"""
import logging
import os
from datetime import datetime

# Define log file name and directory
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)
print(LOG_FILE_PATH)
# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Export a named logger
logger = logging.getLogger("my_app_logger")

"""Testing logging syntax"""
if __name__ == "__main__":
    logging.info("Logging Started")
    # logging.error("Logging Started with error checking tag--Testing levels")
