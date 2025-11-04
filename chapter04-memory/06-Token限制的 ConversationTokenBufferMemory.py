import os

import dotenv
from langchain.memory import ConversationTokenBufferMemory
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
    tiktoken_model_name="gpt-3.5-turbo",  # 用于 token 计数
)

memory = ConversationTokenBufferMemory(llm=chat_model, max_token_limit=20)

memory.save_context(
    {"input": "你好，我叫小明，是一名程序员"}, {"output": "你好，小明，很高兴认识你。"}
)
memory.save_context(
    {"input": "我叫什么名字，是什么职业呢？"}, {"output": "你叫小明，是一名程序员。"}
)
print(memory.load_memory_variables({}))
