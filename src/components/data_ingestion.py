# Common imports
from src.logger import logger
from src.exception import AppException
import sys
import os

import pandas as pd
from dataclasses import dataclass

from sklearn.model_selection import train_test_split

# Main function imports
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
# logger.info("Checking imports in ingestion file")

@dataclass
class DataIngestionConfig:
    train_path:str=os.path.join('artifacts','train.csv')
    test_path:str=os.path.join('artifacts','test.csv')
    raw_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        logger.info("Data Ingestion object initiated successfully")
    
    def initaiate_data_ingestion(self):
        """
            This function is for data ingestion process along with train test split.
            Returns(train_path,test_path)
        """
        logger.info("Data Ingestion initiated")
        try:
            # Read data
            logger.info("Reading data from local datasource")
            df=pd.read_csv('./notebook/data/stud.csv')
            logger.info("Reading successful from local datasource")  
            
            # Create artifacts directry
            logger.info("Creating Artifacts")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_path),exist_ok=True)
            logger.info("Artifacts created successfully")

            # Saving raw data to main source
            logger.info("Saving data to raw")
            df.to_csv(path_or_buf=self.ingestion_config.raw_path,index=False,header=True)
            logger.info("Saving to raw successful")
            
            # Train test split
            logger.info("Train test split initiated")
            train_set,test_set= train_test_split(df,test_size=0.25)  
            logger.info("Train test split successful")
            
            # Saving test data to test data source
            logger.info("Saving test data")
            test_set.to_csv(path_or_buf=self.ingestion_config.test_path,index=False,header=True)
            logger.info("Saving to test successful")
            
            # Saving train data to train data source
            logger.info("Saving train data")
            train_set.to_csv(path_or_buf=self.ingestion_config.train_path,index=False,header=True)
            logger.info("Saving to train successful")
            
            logger.info("Ingestion completed successfully")
            return (self.ingestion_config.train_path,self.ingestion_config.train_path)
        
        except Exception as e:
            logger.error("Error in ingestion process")
            raise AppException(error=e,error_detail=sys)
        
if __name__ in "__main__":
    dataIngestion=DataIngestion()
    train_path,test_path=dataIngestion.initaiate_data_ingestion()
    
    # Data transformation
    dataTransformer=DataTransformation()
    # preprocessor=dataTransformer.get_preprocessor(train_path=train_path,test_path=test_path)
    train_arr,test_arr,preprocessor_path=dataTransformer.transform_data(train_path=train_path,test_path=test_path)
    
    # Model Training
    modelTrainer=ModelTrainer()
    r2_score,pkl_path=modelTrainer.initiate_model_training(test_transformed=test_arr,train_transformed=train_arr)
    