from llms import llm
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from  langchain_community.vectorstores.faiss import FAISS

embedding_for_vector_db = SentenceTransformerEmbeddings(model_name="all-miniLM-L6-v2")
vector_db_path = "faiss_index"

def merge_index(index_selected:str, target:str):
    db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True, index_name=target)

    db2 = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True, index_name=index_selected)

    # print(db.merge_from(db2))
    db.save_local(folder_path=vector_db_path, index_name=target)




