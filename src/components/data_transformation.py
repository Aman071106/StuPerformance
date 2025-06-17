# Common imports
import sys
import os
from src.exception import AppException
from src.logger import logger

# Utils
from src.utils import save_pkl
# test
# logger.info("Checking imports in data_transformation")

# Data transformation imports
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline

from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    preprocessor_pkl_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    """
        This file and class implements data_transformation
    """

    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_preprocessor(self, train_path, test_path):
        """
            Helper to transform data that contains actual transform logic and return the preprocessor.
        """
        logger.info("Initialized Data Transformation")
        try:
            # Read data
            logger.info("Reading train and test data after ingestion")
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)
            logger.info("Reading complete")

            # Dependent and independent features
            logger.info("Splitting features")
            target_column = "math_score"
            X_train = df_train.drop(columns=[target_column])

            # Getting numerical and cateogrical features
            logger.info('Getting numerical and cateogrical features')
            num_features = X_train.select_dtypes(exclude='object').columns
            cat_features = X_train.select_dtypes(include='object').columns

            logger.info(f"Categorical columns: {cat_features}")
            logger.info(f"Numerical columns: {num_features}")
            # Now start transformation
            logger.info("Entering actual transformation phase--creating preprocessor")
            # Numerical features
            num_pipeline = Pipeline(
                [
                    ('simple_imputer', SimpleImputer(strategy='median')),
                    ('scale_numall', StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                [
                    ('ohe_allCat', OneHotEncoder()),
                    ('scale_allCat', StandardScaler(with_mean=False))
                ]
            )
            # ColumnTransformer
            preprocessor = ColumnTransformer(
                [
                    ('num_pipe', num_pipeline, num_features),
                    ('cat_pipe', cat_pipeline, cat_features),

                ],
                remainder='passthrough'  # although no remainder
            )
            return preprocessor

        except Exception as e:
            raise AppException(e, sys)

    # Test in ingestion first then move to transform
    def transform_data(self, train_path, test_path):
        """
            Here actual transformation happens and it returns the pkl file path and scaled data arrays(np arrays)
        """
        try:
            logger.info("Initializing transformation process-- getting preprocessor")
            preprocessor = self.get_preprocessor(
                train_path=train_path, test_path=test_path)

            # Reading data
            logger.info("Reading data...")
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)

            # Spliting
            logger.info(
                "Reading successful...spliting to dependent and independent features")
            target_column = "math_score"
            X_train = df_train.drop(columns=[target_column])
            X_test = df_test.drop(columns=[target_column])
            y_train = df_train[target_column]
            y_test = df_test[target_column]

            # Now transform data
            logger.info("Transformation begins")
            X_train_scaled = preprocessor.fit_transform(X_train)
            X_test_scaled = preprocessor.transform(X_test)

            # Now return and save
            logger.info("Saving pickle object")
            save_pkl(
                file_path=self.transformation_config.preprocessor_pkl_path, pkl_obj=preprocessor
            )
            logger.info("Saved successfully")
            
            logger.info("Returning arrays and pkl file path")
            train_arr=np.column_stack((X_train_scaled,y_train))
            test_arr=np.column_stack((X_test_scaled,y_test))
            
            return (train_arr,test_arr,self.transformation_config.preprocessor_pkl_path)
            
        except Exception as e:
            raise AppException(e,sys)
        
