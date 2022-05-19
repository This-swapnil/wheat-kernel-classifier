import argparse
import os.path

import pandas as pd

from application_logging import logger
from src.utils.all_utils import read_yaml, create_directory

file_object = open("Training_logs/generalLog.txt", "a+")
log_writter = logger.App_logger()


def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path)

    # save dataset in the local directory
    # create path to directory: artifacts/raw_local_dir/data.csv
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    # create directory
    create_directory(dirs=[raw_local_dir_path])
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)

    df.to_csv(raw_local_file_path, index=False)
    log_writter.log(file_object, f"Data downloaded at: {raw_local_file_path}")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default='config/config.yaml')

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)