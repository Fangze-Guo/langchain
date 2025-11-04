import os

import dotenv
from langchain.memory import ConversationSummaryMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

history = ChatMessageHistory()
history.add_user_message("你好，我叫小明，是一名程序员")
history.add_ai_message("你好，小明，很高兴认识你。")

memory = ConversationSummaryMemory.from_messages(
    llm=chat_model,
    chat_memory=history,
)

print(memory.load_memory_variables({}))
