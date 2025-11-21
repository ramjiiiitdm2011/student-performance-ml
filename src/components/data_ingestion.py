import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("notebook", "data", "stud.csv")
    train_data_path: str = os.path.join("notebook", "data", "train.csv")
    test_data_path: str = os.path.join("notebook", "data", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Data Ingestion started")

        try:
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logger.info("Dataset loaded successfully")

            df["average"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3
            logger.info("Average score column created")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            logger.info("Train-test split started")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logger.info("Data Ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logger.error("Error in Data Ingestion")
            raise CustomException(e, sys)
