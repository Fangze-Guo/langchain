import os

import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

response = chat_model.invoke("你好")
print(type(response))  # AIMessage

# 获取输出结果
parser = StrOutputParser()
result = parser.invoke(response)
print(result)