import argparse
from src.utils.all_utils import read_yaml,create_directory,save_local_df
import pandas as pd
import os
import joblib
from application_logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

file_object = open("Training_logs/generalLog.txt", "a+")
log_writter = logger.App_logger()


def split_and_save_data(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    #save data set in the local directory
    #craete path to directory: artifacts/raw_local_dir/data/csv


    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file= config['artifacts']['raw_local_file']
    scaler_dir = config['artifacts']['model_dir']

    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    df = pd.read_csv(raw_local_file_path)

    split_ratio = params['base']['test_size']
    random_state = params['base']['random_state']

    # standard scaling
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    create_directory(dirs=[os.path.join(artifacts_dir,scaler_dir)])
    scaled_data_filename = config['artifacts']['scaled']
    model_path = os.path.join(artifacts_dir,scaler_dir,scaled_data_filename)
    joblib.dump(scaler,model_path)


    train,test = train_test_split(df_scaled,test_size=split_ratio,random_state=random_state)
    log_writter.log(file_object, f"Data splitted into train and test")

    split_data_dir = config['artifacts']['split_data_dir']
    create_directory(dirs=[os.path.join(artifacts_dir,split_data_dir)])

    train_data_filename = config['artifacts']['train']
    test_data_filename = config['artifacts']['test']

    train_data_path = os.path.join(artifacts_dir,split_data_dir,train_data_filename)
    test_data_path = os.path.join(artifacts_dir,split_data_dir,test_data_filename)
    

    for data, data_path in (train, train_data_path),(test,test_data_path):
        save_local_df(data,data_path)




if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default='config/config.yaml')
    args.add_argument("--params", "-p", default='params.yaml')

    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config,params_path=parsed_args.params)