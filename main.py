from sensor.configuration.mongo_db_connection import MongoDBClient
#from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
    
    
    
    # mongodb_client = MongoDBClient()
    # print("Collection names: ",mongodb_client.database.list_collection_names())

    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig(
    #     training_pipeline_config= training_pipeline_config
    # )
    # print(data_ingestion_config.__dict__)

