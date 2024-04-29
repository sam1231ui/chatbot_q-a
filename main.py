import streamlit as st
from chat_bot import get_response, get_chat_answer
import utility
import vectordb

# CHAT BOT SECTION
st.title("Chat bot app")
st.header("Write your Question")
question = st.text_input("start the chat !")


# with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = utility.get_pdf_text(pdf_docs)
#                 vectordb.create_vectordb(raw_text)
#                 st.success("Done")

# verification of question 
if utility.verify_question(question):
    answer = get_response(question)["output_text"]
    # answer = get_chat_answer(question)
    st.header("Answer")
    st.write(answer)
    st.header("Doc Query Data")
    doc_data = vectordb.get_query_data(question)
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
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = vectordb.get_pdf_text(pdf_docs)
                text_chunks = vectordb.get_text_chunks(raw_text)
                vectordb.get_vector_store(text_chunks)
                st.success("Done")