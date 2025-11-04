import os

import dotenv
from langchain.memory import ChatMessageHistory
from langchain_openai import ChatOpenAI

history = ChatMessageHistory()
history.add_user_message("你好，我是小明")
history.add_ai_message("你好，很高兴认识你")
history.add_user_message("你知道我是谁吗？")

print(history.messages)


dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

response = chat_model.invoke(history.messages)
print(response.content)
