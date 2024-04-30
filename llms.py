import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# google gemini llm
api_key = os.getenv("google_api_key")
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, temperature=0.6)