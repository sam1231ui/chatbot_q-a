from langchain_community.vectorstores.faiss import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import csv
from langchain_community.document_loaders.csv_loader import CSVLoader


embedding_for_vector_db = SentenceTransformerEmbeddings(model_name="all-miniLM-L6-v2")
vector_db_path = "faiss_index"

# def create_vectordb():
#     loader = TextLoader('/home/samruddhak/Downloads/state_of_the_union.txt')
#     # data = raw_text
#     print(loader)
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
#     texts = text_splitter.split_documents(loader)
#     vectordb = FAISS.from_documents(texts, embedding_for_vector_db)
#     vectordb.save_local(vector_db_path)

# pdf to text 
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



#creating text chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

#Storing the text chunk
def get_vector_store(text_chunks, file_name):
    name = file_name.split(".")[0]
    vector_store = FAISS.from_texts(text_chunks, embedding=embedding_for_vector_db)
    vector_store.save_local(vector_db_path, index_name=name)

# similar search in faiss
def get_query_data(question, index):
    db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True, index_name=index)
    retriever = db.as_retriever(k=4)
    docs_data = retriever.invoke(question)
    return docs_data

# add data to exisiting faiss
def appent_to_index(text_chunks):
    db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True)
    db.add_texts(texts=text_chunks)
    db.save_local(vector_db_path)

# print(get_query_data("What did the president say about Ketanji Brown Jackson"))
# loader = CSVLoader("/home/samruddhak/Downloads/archive (2)/shakespeare_plays.csv")
# data = loader.load()

# # print(get_csv_text(data))
