# Common imports
from src.exception import AppException
import sys
import os
from src.logger import logger

# specific imports
import dill

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, root_mean_squared_error
from sklearn.model_selection import cross_val_score,GridSearchCV


def save_pkl(file_path, pkl_obj):
    """
        This function save a python object to pickle file.
    """
    logger.info(
        f"Saving pickle object....{pkl_obj}...at file path {file_path}")
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(pkl_obj, file_obj)

    except Exception as e:
        raise AppException(e, sys)

def load_pkl(file_path):
    try:
       with open(file_path, 'rb') as file:
            obj = dill.load(file)
       return obj
    except Exception as e:
        raise AppException(e,sys)

def evaluate_model(modelDict, X_train, X_test, y_train, y_test, paramDictList):
    modelReport = {}
    best_model_obj = None
    best_model_name = None
    best_model_score = float("-inf")
    
    try:
        logger.info("Started model training and evaluation in utils")
        for modelname in modelDict.keys():
            model = modelDict[modelname]
            gs = GridSearchCV(model, param_grid=paramDictList[modelname], cv=5)
            gs.fit(X_train, y_train)
            best_model = gs.best_estimator_

            y_pred = best_model.predict(X_test)
            y_pred_train = best_model.predict(X_train)
            cv_score = cross_val_score(
                estimator=best_model, X=X_train, y=y_train, cv=7, scoring='r2')
            r_2_train = r2_score(y_train, y_pred_train)
            r_2_test = r2_score(y_test, y_pred)

            modelReport[modelname] = {
                'train': {
                    'r2_score': r_2_train,
                    'adj_r2_score': 1-((1-r_2_train)*(X_train.shape[0]-1)/(X_train.shape[0]-X_train.shape[1]-1)),
                    'mae': mean_absolute_error(y_train, y_pred_train),
                    'mse': mean_squared_error(y_train, y_pred_train),
                    'rmse': root_mean_squared_error(y_train, y_pred_train), 
                    'cv_score': cv_score
                },
                'test': {
                    'r2_score': r_2_test,
                    'adj_r2_score': 1-((1-r_2_test)*(X_test.shape[0]-1)/(X_test.shape[0]-X_train.shape[1]-1)),
                    'mae': mean_absolute_error(y_test, y_pred),
                    'mse': mean_squared_error(y_test, y_pred),
                    'rmse': root_mean_squared_error(y_test, y_pred)
                }
            }

            if r_2_test > best_model_score:
                best_model_score = r_2_test
                best_model_name = modelname
                best_model_obj = best_model

        return modelReport, best_model_name, best_model_obj
    except Exception as e:
        raise AppException(e, sys)
