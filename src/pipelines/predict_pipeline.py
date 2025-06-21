# Common imports 
from src.exception import AppException
import sys,os
from src.logger import logger

#utils
from src.utils import load_pkl

# Specific imports
import pandas as pd

class FormData:
    """
        This class responsible for handling user input to df.
    """
    def __init__(self,dataMap):
        self.dataMap=dataMap
    def get_df(self):
        try:
            df=pd.DataFrame(self.dataMap)
            logger.info(df)
            return df
        except Exception as e:
            raise AppException(e,sys)

class Predict:
    """
        This class is responsible for prediction of data on a new datapoint. 
    """
    def __init__(self):
        self.preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
        self.model_path=os.path.join('artifacts','model.pkl')
        
    def predictValue(self,df):
        logger.info("Prediction starts") 

        try:
           preprocessor=load_pkl(file_path=self.preprocessor_path)
           model=load_pkl(file_path=self.model_path)
        #    logger.info(f"{model}")
           transform_arr=preprocessor.transform(df)
           logger.info(f"Transformed arr: {transform_arr}")
           
           predicted=model.predict(transform_arr)
           
           logger.info(f"Predicted= {predicted}")
           return predicted[0]
        except Exception as e:
            raise AppException(e,sys)
        
# test in test.py