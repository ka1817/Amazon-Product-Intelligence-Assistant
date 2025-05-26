import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_preprocess import data_preprocess
from src.query_rewritting import query_rewriting
import warnings
warnings.filterwarnings('ignore')

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def retrival_genaration(query: str):  # Accept query as input
    docs = data_preprocess()
    embedding_model = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(docs, embedding_model)

    llm = ChatGroq(api_key=GROQ_API_KEY, model="gemma2-9b-it")
    
    template = """
You are a helpful assistant that provides answers to user queries based on product information. Use the provided context from the product dataset to craft a clear, concise, and informative answer.

Instructions:
- Base your answer **only** on the retrieved context.
- Include specific product features, benefits, or usage information where relevant.
- If multiple products match the query, briefly describe each.
- If no relevant information is found, say: "Sorry, no matching product information was found in the dataset."

Context:
{context}

Question:
{question}

Answer:
"""
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)

    # Initialize the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", k=3),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    # Rewrite the query using the query_rewriting function
    rewritten_query = query_rewriting(query)

    # Retrieve the top 3 documents (context) based on the rewritten query
    result = qa_chain.invoke({"query": rewritten_query})

    return result["result"]

if __name__ == "__main__":
    query = "Identify a product that offers arch support"
    result = retrival_genaration(query)
    print(result)
