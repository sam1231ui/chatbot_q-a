from llms import llm
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from  langchain_community.vectorstores.faiss import FAISS
import streamlit as st
from langchain.document_loaders.text import TextLoader


embedding_for_vector_db = SentenceTransformerEmbeddings(model_name="all-miniLM-L6-v2")
vector_db_path = "faiss_index"

db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True, index_name="pratiyush_cv")

db2 = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True, index_name="SamruddhaKumbhar_resume")

print(db.merge_from(db2))
db.save_local(folder_path=vector_db_path, index_name="pratiyush_cv")




