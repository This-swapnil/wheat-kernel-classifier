from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB

from src.utils.all_utils import read_yaml,create_directory,save_local_df
import argparse
import os
from application_logging import logger
import pandas as pd
import joblib

file_object = open("Training_logs/TrainingLog.txt", "a+")
log_writter = logger.App_logger()

def get_best_params_for_naive_bayes(train_x,train_y,params,verbose,cv):
    log_writter.log(file_object, f"Entered the get_best_params_for_naive_bayes method of stage_03_train.py")
    param_grid = params
    gnb = GaussianNB()
    grid = GridSearchCV(estimator=gnb,param_grid=param_grid,cv = cv,verbose=verbose)
    grid.fit(train_x,train_y)

    pass

def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_dir']
    train_data_filename = config['artifacts']['train']

    split_data_dir = config['artifacts']['split_data_dir']

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    train_data = pd.read_csv(train_data_path)
    train_x = train_data.drop(columns=['seedType'])
    train_y = train_data['seedType']