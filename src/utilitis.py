import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging

def save_object(obj, file_path):
    """
    Saves a Python object to the specified file path using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        logging.info(f"Object saved successfully at {file_path}")
        return file_path
    except Exception as e:
        raise CustomException(e, sys)