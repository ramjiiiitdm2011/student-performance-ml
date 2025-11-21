import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import get_logger
from src.utils import save_object

logger = get_logger(__name__)


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def evaluate_models(self, X_train, y_train, X_test, y_test, models):
        scores = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            scores[name] = r2_score(y_test, y_pred)
        return scores

    def initiate_model_training(self, X_train, y_train, X_test, y_test):
        try:
            logger.info("Model Training started")

            models = {
                "LinearRegression": LinearRegression(),
                "RandomForest": RandomForestRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
            }

            model_scores = self.evaluate_models(X_train, y_train, X_test, y_test, models)
            logger.info(f"Model Scores: {model_scores}")

            # Select BEST model
            best_model_name = max(model_scores, key=model_scores.get)
            best_model = models[best_model_name]

            logger.info(f"Best Model: {best_model_name}")

            # Save best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logger.info("Best model saved successfully")

            return best_model_name, model_scores[best_model_name]

        except Exception as e:
            logger.error("Error in Model Training")
            raise CustomException(e, sys)
