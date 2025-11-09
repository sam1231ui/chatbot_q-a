# 🤖 Personal GenAI Chatbot

This is a fully open-source GenAI chatbot built using **Streamlit**, **LangChain**, and **Hugging Face models**. It answers questions about your **GitHub profile**, **LinkedIn (PDF export)**, and **Resume**, using intelligent agents that dynamically fetch and process your data.

## ✨ Features

- 🔍 Uses **LangChain agents** to interact with:
  - GitHub (via API)
  - LinkedIn profile (PDF)
  - Resume (PDF)
- 🧠 Uses a **free open-source LLM (GPT-J)** for response generation
- 💡 Embedded within a simple and fast **Streamlit UI**
- 🔄 “Refresh Profile Data” button to re-fetch data anytime
- 💬 Ask questions like:
  - _“What are my top GitHub projects?”_
  - _“List my key skills from LinkedIn.”_
  - _“Summarize my work experience from resume.”_

---

## 🧱 Project Structure

--->Streamlit UI
----> Agent: Fetch & Parse +GitHub via API + LinkedIn via PDF + Resume from blob/local 
------> Chunk & Embed (SBERT + FAISS) 
---------> LLM Q&A Logic
 


## 🛡 Limitations & Disclaimer
LinkedIn PDF parsing might miss some structured info due to formatting

GPT-J requires decent hardware to run locally (16GB+ RAM recommended)

This is a personal project and not affiliated with LinkedIn, GitHub, or OpenAI
