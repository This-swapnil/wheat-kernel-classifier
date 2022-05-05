import os

import yaml

from application_logging import logger

file_object = open("Training_logs/generalLog.txt", "a+")
log_writter = logger.App_Logger()


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content


def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        log_writter.log(file_object, f"Directory is Created at: {dir_path}")
        print(f"Directory is Created at: {dir_path}")


def save_local_df(data, data_path, index_status=False, sep=","):
    data.to_csv(data_path, index=index_status, sep=sep)
    log_writter.log(file_object, f"data is saved at{data_path}")
    print(f"data is saved at{data_path}")