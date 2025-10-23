import os

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}"),
        ("human", "{input}"),
    ]
)

parser = JsonOutputParser()

# 构建chain
chain = chat_prompt_template | chat_model | parser

# 调用chain时传入参数
result = chain.invoke(
    {
        "role": "AI专家",
        "input": "大模型中的LangChain是什么？用JSON格式回复，问题用question, 回答用 anser",
    }
)

print(result)
