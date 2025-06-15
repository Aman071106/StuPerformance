"""
    This is a test file
"""
from src.exception import AppException
import sys
from src.logger import logger


#Test logging
logger.info("Testing successful in test.py")

#Exception Testing
try:
    2/0
except Exception as e:
    logger.error(e)
    raise AppException(e,sys)

