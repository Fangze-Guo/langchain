import os

import dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

# 通过 Chat 提示词模板，创建提示词
chat_prompt_template = ChatPromptTemplate.from_messages(
    [("system", "你是一个AI助手，名字叫{name}"), ("human", "我的问题是{question}")]
)

prompt = chat_prompt_template.invoke({"name": "小明", "question": "1 + 2 * 3 = ?"})

# 通过大模型调用
response = chat_model.invoke(prompt)
print(response.content)
