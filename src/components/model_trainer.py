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
    trained_model_file_path=os.path.join("artifacts","model")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            exp_name = setup(data =X_train,  target = y_train,fix_imbalance=True,use_gpu=True)
            best_model = compare_models()
            best_model = tune_model(best_model, choose_better = True)
            save_model(best_model,self.model_trainer_config.trained_model_file_path)
            logging.info("Model training Sucessfully")

            return "Model Training Sucessfully Done"

        except Exception as e:
            raise CustomException(e,sys)

