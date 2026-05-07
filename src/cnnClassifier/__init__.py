import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
os.makedirs("log_dir", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler("log_dir/file.log"),
        logging.StreamHandler(sys.stdout)
    ]   
)

logger=logging.getLogger("cnnClassifierLogger")