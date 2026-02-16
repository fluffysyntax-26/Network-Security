import logging
import os
from datetime import datetime

# Create logs directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Safe filename (NO / or :)
LOG_FILE = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

# Final log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)