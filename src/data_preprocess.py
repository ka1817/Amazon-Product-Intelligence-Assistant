import pandas as pd
from src.data_ingestion import data_ingestion
from langchain.schema import Document

def data_preprocess():
    df = data_ingestion()
    df.dropna(axis=0, inplace=True)
    df["content"] = df["Title"] + ". " + df["Description"] + ". " + df["Category"]
    docs = [Document(page_content=row["content"]) for _, row in df.iterrows()]
    return docs

if __name__ == "__main__":
    print(data_preprocess())
