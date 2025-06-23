import logging
import os
import sys
from datetime import datetime

# Generate a log filename with a timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create a logs folder (not including filename)
logs_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Set up logging: logs to file + prints to terminal
logging.basicConfig(
    level=logging.INFO,
    format=" [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)
