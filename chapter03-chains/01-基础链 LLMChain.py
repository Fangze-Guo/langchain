import os

import dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [("system", "你是一个数学高手"), ("human", "帮我解决{question}")]
)

chain = LLMChain(
    llm=chat_model,
    prompt=chat_prompt_template,
    verbose=True,   # 打印详细日志信息
)

result = chain.invoke(input={"question": "1+1*2=?"})
print(result)
