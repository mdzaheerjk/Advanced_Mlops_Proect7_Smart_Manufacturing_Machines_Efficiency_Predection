import os
import joblib
from sklearn.linear_model import LogisticRegression
from src.logger import get_logger
from src.custom_exception import CustomException
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self,processed_data_path , model_output_path):
        self.processed_path = processed_data_path
        self.model_path = model_output_path
        self.clf = None
        self.X_train, self.X_test , self.y_train , self.y_test = None , None , None , None

        os.makedirs(self.model_path,exist_ok=True)
        logger.info("Model Training initialized...")

    def load_data(self):
        try:
            self.X_train = joblib.load(os.path.join(self.processed_path , "X_train.pkl"))
            self.X_test = joblib.load(os.path.join(self.processed_path , "X_test.pkl"))
            self.y_train = joblib.load(os.path.join(self.processed_path , "y_train.pkl"))
            self.y_test = joblib.load(os.path.join(self.processed_path , "y_test.pkl"))

            logger.info("Data loaded sucesfuly...")
        
        except Exception as e:
            logger.error(f"Error while loading data {e}")
            raise CustomException("Failed to load data" , e)
        
    def train_model(self):
        try:
            self.clf = LogisticRegression(random_state=42,max_iter=1000)
            self.clf.fit(self.X_train,self.y_train)

            joblib.dump(self.clf , os.path.join(self.model_path , "model.pkl"))

            logger.info("Model trained and saved sucesfuly...")

        except Exception as e:
            logger.error(f"Error while training model {e}")
            raise CustomException("Failed to train model" , e)
        
    def evaluate_model(self):
        try:
            y_pred = self.clf.predict(self.X_test)

            accuracy = accuracy_score(self.y_test,y_pred)
            precision =  precision_score(self.y_test,y_pred , average="weighted")
            recall =  recall_score(self.y_test,y_pred , average="weighted")
            f1 =  f1_score(self.y_test,y_pred , average="weighted")

            logger.info(f"Accuracy : {accuracy}")
            logger.info(f"Precision Score : {precision}")
            logger.info(f"Recall Score : {recall}")
            logger.info(f"F1 Score : {f1}")

            logger.info("Model Evaluation Done..")

        except Exception as e:
            logger.error(f"Error while evaluating model {e}")
            raise CustomException("Failed to evaluate model" , e)
        
    def run(self):
        self.load_data()
        self.train_model()
        self.evaluate_model()

if __name__=="__main__":
    trainer = ModelTraining("artifacts/processed/" , "artifacts/models/")
    trainer.run()
        

