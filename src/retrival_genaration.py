import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
load_dotenv()

from src.data_preprocess import data_preprocess
from src.query_rewritting import query_rewriting

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import warnings
warnings.filterwarnings('ignore')

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ingestdata():
    docs = data_preprocess()
    embedding_model = HuggingFaceEmbeddings(model_name="thenlper/gte-small")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    return vectorstore

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
    You are a helpful assistant that provides answers to user queries based on product information.
    Use the provided context from the product dataset to craft a clear, concise, and informative answer.

    Instructions:
    - Base your answer **only** on the retrieved context.
    - Include specific product features, benefits, or usage information where relevant.
    - If multiple products match the query, briefly describe each.
    - If no relevant information is found, say: "Sorry, no matching product information was found in the dataset."

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
    llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")  # use correct model name

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__ == "__main__":
    vstore = ingestdata()
    chain = generation(vstore)

    query = "Identify a product that offers arch support"
    rewritten_query = query_rewriting(query)

    response = chain.invoke(rewritten_query)
    print(f"Response: {response}")
