from data_preprocess import data_preprocess
import pandas as pd
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.document_loaders import DataFrameLoader
from langchain.schema import Document
from query_rewritting import query_rewriting
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

from data_ingestion import data_ingestion

def retrival_genaration():
    df=data_ingestion()
    docs=data_preprocess()
    embedding_model = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(docs, embedding_model)

    llm = ChatGroq(api_key=GROQ_API_KEY,model='gemma2-9b-it')
    qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", k=3),
    return_source_documents=True
    )

    return qa_chain

if __name__=='__main__':
    qa_chain=retrival_genaration()
    query = query_rewriting("Identify a product from the dataset that offers arch support. What are its features?")

    response = qa_chain.invoke(query)

    print("Answer:\n", response["result"])

