import os

import dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)


def chat_with_model(question):
    # 提供提示词模板
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个人工智能助手"),
        ("human", "{question}"),
    ])

    while True:
        chain = prompt_template | chat_model
        response = chain.invoke({"question": question})

        print(response.content)

        # 继续获取用户问题
        user_input = input("你还有其他问题吗？")
        if user_input == "q":
            break

        prompt_template.messages.append(AIMessage(content=response.content))
        prompt_template.messages.append(HumanMessage(content=user_input))  

chat_with_model("你好")
