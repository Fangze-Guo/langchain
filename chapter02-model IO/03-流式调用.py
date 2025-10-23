import os

import dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
    streaming=True,
)

message = [HumanMessage(content="你好, 请介绍一下自己")]

response = chat_model.stream(message)
for chunk in response:
    print(chunk.content, end="", flush=True)
