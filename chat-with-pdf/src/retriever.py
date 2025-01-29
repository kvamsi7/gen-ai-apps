from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_history_aware_retriever_chain(llm, retriever):
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question,"
        " which might reference context in the chat history, "
        "formulate a standalone question which can be understood"
        " without the chat history. Do not answer the question, "
        "just reformulate if needed or return as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    return history_aware_retriever
