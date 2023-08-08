from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template(
            "Is the company {input} a black listed company by the US customs?"
        )
    ]
)

llm = ChatOpenAI(temperature=0.9, max_tokens=100)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, llm=llm, prompt=prompt)


if __name__ == "__main__":
    print(conversation.run(input="Huawei"))
    # "Is the company Huawei a black listed company by the US customs?
    # Yes, Huawei is a black listed company by the US customs."
