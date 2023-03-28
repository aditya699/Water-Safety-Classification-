import os
import sys
from dataclasses import dataclass
from pycaret.classification import *
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            train_array=pd.DataFrame(train_array)
            test_array=pd.DataFrame(test_array)
            exp_name = setup(data = train_array,  target = 'is_safe',fix_imbalance=True,test_data=test_array)
            best_model = compare_models()
            save_model(best_model,self.model_trainer_config.trained_model_file_path)
            logging.info("Model training Sucessfully")

            return "Model Training Sucessfully Done"

        except Exception as e:
            raise CustomException(e,sys)

