from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from llms import llm
import vectordb



prompt_template = """
  Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
  provided context then, "answer it on your best understanding"\n\n
  Context:\n {context}?\n
  Question: \n{question}\n

  Answer:
"""

prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])

# question_answering_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Answer the user's questions based on the below context:\n\n{context}",
#         ),
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )

# document_chain = create_stuff_documents_chain(llm, question_answering_prompt)
chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

# answer with vectordb
def get_response(question):
    docs = vectordb.get_query_data(question)
    # demo = ChatMessageHistory()
    # demo.add_user_message(question)

    # answer =document_chain.invoke(
    #             {
    #                 "messages": demo.messages,
    #                 "context": docs,
    #             }
    #         )
    answer = chain({
        "input_documents": docs,
        "question":question
        },return_only_outputs=True
    )
    
    return answer

# anwer without vector db
def get_chat_answer(question):
    return llm.invoke(question).content

# get_response("What did the president say about Ketanji Brown Jackson ?")