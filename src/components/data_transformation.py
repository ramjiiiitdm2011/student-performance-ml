import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import get_logger
from src.utils import save_object

logger = get_logger(__name__)


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        """
        Creates preprocessing pipeline for:
        - OneHotEncoding (categorical)
        - StandardScaler (numerical)
        """
        try:
            logger.info("Preparing data transformation pipeline")

            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            numerical_columns = [
                "math_score",
                "reading_score",
                "writing_score"
            ]

            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )

            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            # Combine pipelines
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns),
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logger.info("Data Transformation started")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info("Train and Test data loaded")

            # Target column
            target_column = "average"
            input_columns = [col for col in train_df.columns if col != target_column]

            X_train = train_df[input_columns]
            y_train = train_df[target_column]

            X_test = test_df[input_columns]
            y_test = test_df[target_column]

            preprocessor = self.get_data_transformation_object()

            logger.info("Applying preprocessing pipeline")

            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)

            # Save preprocessor
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )

            logger.info("Preprocessor saved successfully")

            return (
                X_train_transformed,
                X_test_transformed,
                y_train,
                y_test,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            logger.error("Error in Data Transformation")
            raise CustomException(e, sys)
