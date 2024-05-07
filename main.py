import streamlit as st
from chat_bot import get_response, get_chat_answer
import utility
import vectordb, os, index_utility
import pandas as pd


# CHAT BOT SECTION
st.title("Q&A chatbot !!")
st.header("Write your Question")

question = st.text_input("start the chat !")
if not question:
    st.text("step 1- Load document and press submit\nstep 2- select your uploaded document to use\nstep 3- Ask questions !! \n")

    
# Sidebar - Index File Selection
st.sidebar.title("FAISS Vector database:")
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
    # st.header("Doc Query Data")
    # doc_data = vectordb.get_query_data(question, selected_file)
    # st.write(doc_data)
# else:
#     st.warning("must be 2 to 100 chareacters !!")



# sidebar features section 
with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        
        # Saving the uploaded file:
        # if pdf_docs is not None:
        #     save_button = st.button("Save Files")
        #     if save_button:
        #         target_folder = "uploaded_files"

        #         if pdf_docs.name.split(".")[1] not in ["csv", "pdf"]:
        #             st.warning("Please upload only pdf or csv files") 
        #         else :
        #             utility.save_uploaded_file(pdf_docs) 
        #             st.success("Files saved successfully")
            
        # Vectordb creating 
        if st.button("submit & process") and pdf_docs:
            extension = pdf_docs[0].name.split(".")[1]

            if extension == "pdf":
                with st.spinner("Processing..."):
                    raw_text = vectordb.get_pdf_text(pdf_docs)
                    text_chunks = vectordb.get_text_chunks(raw_text)
                    vectordb.get_vector_store(text_chunks, pdf_docs[0].name)
                    st.success("Done")
                    st.experimental_rerun()

            elif extension == "csv":
                with st.spinner("Processing..."):
                    # raw_text = vectordb.get_csv_text()
                    text_chunks = vectordb.get_text_chunks(pd.read_csv(pdf_docs).to_string())
                    vectordb.get_vector_store(text_chunks, pdf_docs[0].name)
                    st.success("Done")
                    # vectordb.appent_to_index(text_chunks)
                    st.experimental_rerun()
            else :
                st.warning("please upload csv or pdf")
        else:
            st.warning("please upload file")

        # Adding the data to exsisting vector db
        # if st.button("Add data to exisiting Faiss db"):
        #     with st.spinner("Processing..."):
        #         raw_text = vectordb.get_pdf_text(pdf_docs)
        #         text_chunks = vectordb.get_text_chunks(raw_text)
        #         vectordb.appent_to_index(text_chunks)
        #         st.success("Done")

        # Merge feature of index section
        # st.header("Merge index:")
        # index_selected = st.sidebar.selectbox("index to merge", set(files_names))
        # target_index = st.sidebar.selectbox("target index", set(files_names))

        # if index_selected == target_index:
        #     st.warning("please select different names from the list")
        # else :
        #     if st.button("Merge"):
        #         with st.spinner("Processing..."):
        #             index_utility.merge_index(index_selected=index_selected, target=target_index)
        #             st.success("Done")