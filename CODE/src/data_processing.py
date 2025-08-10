import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self,input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
        self.features = None

        os.makedirs(self.output_path,exist_ok=True)
        logger.info("Data Processing initalized...")

    def load_data(self):
        try:
            self.df = pd.read_csv(self.input_path)
            logger.info("Data loaded sucesfully...")
        except Exception as e:
            logger.error(f"Error while loading data {e}")
            raise CustomException("Failed to load data",e)
        
    def preprocess(self):
        try:
            self.df["Timestamp"] = pd.to_datetime(self.df["Timestamp"] , errors='coerce')
            categorical_cols = ['Operation_Mode','Efficiency_Status']
            for col in categorical_cols:
                self.df[col] = self.df[col].astype('category')

            self.df["Year"] = self.df["Timestamp"].dt.year
            self.df["Month"] = self.df["Timestamp"].dt.month
            self.df["Day"] = self.df["Timestamp"].dt.day

            self.df["Hour"] = self.df["Timestamp"].dt.hour

            self.df.drop(columns=["Timestamp","Machine_ID"] , inplace=True)

            columns_to_encode = ["Efficiency_Status","Operation_Mode"]
            for col in columns_to_encode:
                le = LabelEncoder()
                self.df[col] = le.fit_transform(self.df[col])

            logger.info("All basic data preprocessing done..")
        
        except Exception as e:
            logger.error(f"Error while preprocessing data {e}")
            raise CustomException("Failed to preprocess data",e)
        
    def split_and_scale_and_save(self):
        try:
            self.features = [
                'Operation_Mode', 'Temperature_C', 'Vibration_Hz',
                'Power_Consumption_kW', 'Network_Latency_ms', 'Packet_Loss_%',
                'Quality_Control_Defect_Rate_%', 'Production_Speed_units_per_hr',
                'Predictive_Maintenance_Score', 'Error_Rate_%','Year', 'Month', 'Day', 'Hour'
            ]

            X = self.df[self.features]
            y = self.df["Efficiency_Status"]

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            X_train , X_test , y_train , y_test = train_test_split(X_scaled,y, test_size=0.2 , random_state=42 , stratify=y)

            joblib.dump(X_train , os.path.join(self.output_path , "X_train.pkl"))
            joblib.dump(X_test , os.path.join(self.output_path , "X_test.pkl"))
            joblib.dump(y_train , os.path.join(self.output_path , "y_train.pkl"))
            joblib.dump(y_test , os.path.join(self.output_path , "y_test.pkl"))

            joblib.dump(scaler , os.path.join(self.output_path , "scaler.pkl"))
            logger.info("All things saved sucesfully for Data processing..")

        except Exception as e:
            logger.error(f"Error while split scale and save data {e}")
            raise CustomException("Failed to spli sacle and save data",e)
        
    def run(self):
        self.load_data()
        self.preprocess()
        self.split_and_scale_and_save()

if __name__=="__main__":
    processor = DataProcessing("artifacts/raw/data.csv" , "artifacts/processed")
    processor.run()


        
            

