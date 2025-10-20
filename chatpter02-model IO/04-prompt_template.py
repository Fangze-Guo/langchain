import os

import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

# 提示词模板
prompt_template = PromptTemplate.from_template(
    template="你是{role}，名字为{name}，请介绍一下自己",
)

prompt = prompt_template.invoke(input={"role": "老师", "name": "张三"})

response = chat_model.invoke(prompt)
print(response.content)
