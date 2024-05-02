import streamlit as st
from chat_bot import get_response, get_chat_answer
import utility
import vectordb, os
import pandas as pd

# CHAT BOT SECTION
st.title("Q&A chatbot !!")
st.header("Write your Question")
question = st.text_input("start the chat !")

    
# Sidebar - Index File Selection
st.sidebar.header("Select a vector db to search from")
folder_path = "./faiss_index"
files = os.listdir(folder_path)
files_names = utility.get_files_name(files)
selected_file = st.sidebar.selectbox("Select a file", set(files_names))


# verification of question 
if utility.verify_question(question):
    answer = get_response(question, selected_file)["output_text"]
    # answer = get_chat_answer(question)
    st.header("Answer")
    st.write(answer)
    st.header("Doc Query Data")
    doc_data = vectordb.get_query_data(question, selected_file)
    st.write(doc_data)
else:
    st.warning("must be 2 to 100 chareacters !!")



# file uploading section
with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

       
        # Saving the uploaded file:
        if pdf_docs is not None:
            save_button = st.button("Save Files")
            if save_button:
                target_folder = "uploaded_files"
                saved_file_paths = utility.save_uploaded_file(pdf_docs)
                st.success(f"Files saved successfully at: {', '.join(saved_file_paths)}")
            
        # Vectordb creating 
        if st.button("Make new vector db"):
            with st.spinner("Processing..."):
                raw_text = vectordb.get_pdf_text(pdf_docs)
                text_chunks = vectordb.get_text_chunks(raw_text)
                vectordb.get_vector_store(text_chunks, pdf_docs[0].name)
                st.success("Done")

         # Vectordb creating for csv
        if st.button("Make new vector db of csv"):
            with st.spinner("Processing..."):
                # raw_text = vectordb.get_csv_text()
                text_chunks = vectordb.get_text_chunks(pd.read_csv(pdf_docs[0]).to_string())
                vectordb.get_vector_store(text_chunks, pdf_docs[0].name)
                st.success("Done")

        # Vectordb creating 
        if st.button("Add data to exisiting vector db"):
            with st.spinner("Processing..."):
                raw_text = vectordb.get_pdf_text(pdf_docs)
                text_chunks = vectordb.get_text_chunks(raw_text)
                vectordb.appent_to_index(text_chunks)
                st.success("Done")

        


# files = utility.get_all_files("faiss_index/")

# for file in files:
#   st.write(file)
