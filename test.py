"""
    This is a test file
"""
from src.exception import AppException
import sys
from src.logger import logger

from src.pipelines.predict_pipeline import Predict,FormData

#Test logging
# logger.info("Testing successful in test.py")

#Exception Testing
# try:
#     2/0
# except Exception as e:
#     logger.error(e)
#     raise AppException(e,sys)


# Testing predictPipeline
# stuRecord={
#     "gender": ["female"],
#     "race_ethnicity": ["group C"],
#     "parental_level_of_education": ["associate's degree"],
#     "lunch": ["free/reduced"],
#     "test_preparation_course": ["completed"],
#     "reading_score": [67],
#     "writing_score": [69]
# }
# # female,group C,associate's degree,free/reduced,completed,68,67,69
# formdata=FormData(stuRecord)
# df=formdata.get_df()
# predictor=Predict()
# logger.info(predictor.predictValue(df))
