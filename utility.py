from PyPDF2 import PdfReader
import os

# verify the question
def verify_question(question:str):
    if question is None:
        return False
    if not isinstance(question, str):
        return False
    if len(question) < 2 or len(question) > 100:
        return False
    if not question.strip():  # Check if the string is empty or contains only whitespace
        return False
    return True


# save uploaded file
def save_uploaded_file(uploaded_files):
    target_folder = "uploaded_files"
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    saved_file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(target_folder, uploaded_file.name)
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        saved_file_paths.append(file_path)
    return saved_file_paths


def get_all_files(directory):
  files = []
  for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
      files.append(file)
  return files

def get_files_name(files):
    names = []
    for file in files:
        names.append(file.split(".")[0])
    return names

# files = os.listdir('./faiss_index')
# print(get_files_name(files))