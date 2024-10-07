from stc.embedding_model import embeddings
from langchain_chroma import Chroma 
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from stc.model import model
from langchain.prompts import PromptTemplate
from langchain.agents import Tool


loader = PyPDFDirectoryLoader(r"C:\Users\DebadattaNayak\Desktop\chatbot\data")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
split_text = text_splitter.split_documents(documents)

vectordb = Chroma.from_documents(documents=split_text, embedding=embeddings) 

prompt=PromptTemplate.from_template(template="use this tool only for fetching data on brightspeed")

def get_vectordb_tool():
    tool=Tool(
        func=vectordb.similarity_search,
        name='brightspeed data',
        description="contains info related to brightspeed.Use this tool only when the question is related to Brightspeed",
        retriver_top_k=3
    )
    return tool