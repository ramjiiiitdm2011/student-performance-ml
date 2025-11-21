from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    transform = DataTransformation()
    X_train, X_test, y_train, y_test, _ = transform.initiate_data_transformation(train_path, test_path)

    trainer = ModelTrainer()
    best_model, best_score = trainer.initiate_model_training(X_train, y_train, X_test, y_test)

    print("Best Model:", best_model)
    print("R2 Score:", best_score)
