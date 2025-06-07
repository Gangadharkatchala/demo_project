import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", log_file)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

log_file_path = os.path.join(os.getcwd(), "logs", log_file)
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



    