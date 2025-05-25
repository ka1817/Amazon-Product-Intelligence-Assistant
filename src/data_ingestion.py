import pandas as pd 
import os
def data_ingestion():
    base_dir = os.path.dirname(os.path.dirname(__file__))  
    file_path = os.path.join(base_dir, "data", "amazon_product.csv")
    df=pd.read_csv(file_path)
    return df
data_ingestion()