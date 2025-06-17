# Common imports
from src.exception import AppException
import sys,os
from src.logger import logger

# specific imports
import dill

def save_pkl(file_path,pkl_obj):
    logger.info(f"Saving pickle object....{pkl_obj}...at file path {file_path}")
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(pkl_obj, file_obj)

    except Exception as e:
        raise AppException(e, sys)