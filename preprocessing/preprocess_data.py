from utils import get_root_dir
import pandas as pd
import os

class DataImporter(object):
    """
    Imports dataset
    """
    def __init__(self, dataset_name: str, data_scaling: bool = False, **kwargs):
        data_dir = get_root_dir().joinpath('data')

        train = pd.read_parquet(data_dir.joinpath(f'{dataset_name}/train_targets.parquet'))
       
        X_test_estimated = pd.read_parquet(data_dir.joinpath(f'{dataset_name}/X_test_estimated.parquet'))
       
        X_train_observed = pd.read_parquet(data_dir.joinpath(f'{dataset_name}/train_targets.parquet'))
        
         
class DataSet:
    def __init__(self,
                 dataset_importer: DataImporter,
                 kind: str,
                 **kwargs):
        """
        kind: observerd, estimated, train
        """

        pass


        