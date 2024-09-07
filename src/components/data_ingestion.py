#Typical Data Ingestion Steps
#Data Collection: Gathering data from various sources (e.g., databases, APIs, files).
#Data Loading: Importing the collected data into a storage system or data pipeline.
#Data Transformation: Optionally, transforming the data into the required format or structure.
import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
@dataclass
class DataIngestConfig:
    ## all the  train data/output will be stored in the artifact folder
    train_data_path=os.path.join('artificat','train.csv')
    test_data_path=os.path.join('artificat','test.csv')
    raw_data_path=os.path.join('artificat','raw.csv')
    def __init__(self):
        self.ingestion_config =DataIngestConfig()
        def inititae_data_ingest(self):
            logging.info("Entered into the data ingestion method !")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Reading the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            ### train/test split
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
    ## all the  train data/output will be stored in the artifact folder
    train_data_path=os.path.join('artificat','train.csv')
    test_data_path=os.path.join('artificat','test.csv')
    raw_data_path=os.path.join('artificat','raw.csv')
    if __name__=="__main__":
        obj=DataIngestion()
        train_data,test_data=obj.initiate_data_ingestion()

        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

        modeltrainer=ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    
