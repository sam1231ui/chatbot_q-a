from llms import llm
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from  langchain_community.vectorstores.faiss import FAISS
import streamlit as st
from langchain.document_loaders.text import TextLoader


embedding_for_vector_db = SentenceTransformerEmbeddings(model_name="all-miniLM-L6-v2")
vector_db_path = "faiss_index"

db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True)


retriever = db.as_retriever(k=2)

data = TextLoader('/home/samruddhak/Downloads/state_of_the_union.txt')

async def add(data):
  # Add the documents to the database.
  await print(db.add_documents(data))
  pass

add(data)

def get_docs(question):
    docs_data = retriever.get_relevant_documents(question)
    # docs_data = retriever.invok(question)
    return docs_data


st.header("vector DB different search")
question = st.text_input("Enter to search in vectorstore")

ans = get_docs(question)
st.write(ans)