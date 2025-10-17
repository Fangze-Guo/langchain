import os

import dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(model="deepseek-chat")

system_message = SystemMessage(content="你是一个英语教学专家")
human_message = HumanMessage(content="帮我指定一个英语六级学习计划")

messages = [system_message, human_message]

response = chat_model.invoke(messages)
print(response.content)
