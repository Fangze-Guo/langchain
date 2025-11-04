import os

import dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

prompt_template = PromptTemplate.from_template(
    template="你可以与人类对话。 当前对话历史：{history} 当前问题：{input} ，给出回答。"
)

chain = ConversationChain(llm=chat_model, prompt=prompt_template)

result = chain.invoke(input={"input": "你好，我叫小明，是一名程序员"})
print(result)

result = chain.invoke(input={"input": "我叫什么名字，是什么职业呢？"})
print(result)
