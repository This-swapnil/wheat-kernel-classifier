import pandas as pd

from src.utils.all_utils import read_yaml


def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path, sep=" ")

    # save dataset in the local directory
    # create path to directory: artifacts/