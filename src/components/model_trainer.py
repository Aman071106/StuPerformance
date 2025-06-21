# Common imports
from src.exception import AppException
import sys
import os
from src.logger import logger

# Utils required
from src.utils import save_pkl, evaluate_model
from dataclasses import dataclass

# Specific imports
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor as xgb
from catboost import CatBoostRegressor as ctb

from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error, mean_absolute_error
# logger.info("Imports are perfect")


@dataclass
class ModelTrainerConfig:
    model_pkl_path = os.path.join("artifacts", 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        self.model_dict = {
            # 'lr': LinearRegression(),
            # 'ridge':Ridge(),
            # 'lasso':Lasso(),
            # 'elasticNet': ElasticNet(),
            # 'svr': SVR(),
            # 'knr': KNeighborsRegressor(),
            # 'dtr': DecisionTreeRegressor(),
            'rfr': RandomForestRegressor(),
            'abr': AdaBoostRegressor(),
            'gbr': GradientBoostingRegressor(),
            'xgb': xgb(),
            'ctb': ctb(verbose=False)
        }
        self.paramDictList = {
            'rfr': {'n_estimators': [8, 16, 32, 64, 128, 256]},
            'xgb': {'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]},
            'gbr': {'learning_rate': [.1, .01, .05, .001],
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'n_estimators': [8, 16, 32, 64, 128, 256]},
            'ctb': {'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]},
            'abr': { 'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]},
            # 'lr': {
                
            # }
        }

    def initiate_model_training(self, train_transformed, test_transformed):
        """
            This function is responsible for training on scaled data and returning model pkl file path along with r2_score of model.
            Inputs:
            train,test arr which are np arrays returned by transformation class.
        """
        logger.info("Initiating training")
        try:
            logger.info("Splitting X,y in train and test data")
            X_train, y_train = train_transformed[:,
                                                 :-1], train_transformed[:, -1]
            X_test, y_test = test_transformed[:, :-1], test_transformed[:, -1]
            logger.info("Split successful -Getting model report")
            report, best_model_name, best_model = evaluate_model(
                modelDict=self.model_dict, X_test=X_test, X_train=X_train,
                y_test=y_test, y_train=y_train, paramDictList=self.paramDictList
            )

            logger.info(f"🗒️Report:\n{report}")

            max_r2_score = report[best_model_name]['test']['r2_score']
            if max_r2_score < 0.6:
                raise AppException("Model performance very less exception", sys)

            logger.info(f"Model found with r2_score: {max_r2_score}")
            logger.info(f"Best model: {best_model_name} -- Saving pickle")

            save_pkl(
                file_path=self.model_trainer_config.model_pkl_path,
                pkl_obj=best_model
            )

            logger.info("Model Training successful")
            return (max_r2_score, self.model_trainer_config.model_pkl_path)

        except Exception as e:
            raise AppException(e, sys)
