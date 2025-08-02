import sys
from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataindestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataindestionconfig)
        logging.info("enter try block")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)