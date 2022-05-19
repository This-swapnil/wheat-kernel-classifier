from src.utils.all_utils import read_yaml,create_directory,save_local_df
import argparse
import os
import pandas as pd
import joblib

def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    