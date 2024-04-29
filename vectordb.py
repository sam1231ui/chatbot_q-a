from langchain_community.vectorstores.faiss import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader


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
def get_vector_store(text_chunks):
    vector_store = FAISS.from_texts(text_chunks, embedding=embedding_for_vector_db)
    vector_store.save_local(vector_db_path)

def get_query_data(question):
    db = FAISS.load_local(folder_path=vector_db_path, embeddings=embedding_for_vector_db, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(k=4)
    docs_data = retriever.invoke(question)
    return docs_data


# print(get_query_data("What did the president say about Ketanji Brown Jackson"))