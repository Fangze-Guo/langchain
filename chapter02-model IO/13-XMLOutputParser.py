import os

import dotenv
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

actor_query = "周星驰的简短电影记录"

# 定义 XML 解析器
parser = XMLOutputParser()

# 提示词模板
prompt_template = PromptTemplate.from_template(
    template="用户问题：{query}\n使用的格式：{format_instructions}"
)

prompt = prompt_template.partial(format_instructions=parser.get_format_instructions())

response = chat_model.invoke(prompt.invoke(input={"query": actor_query}))
print(response.content)

result = parser.invoke(response)    # 将 xml 格式解析为易于处理的类似 json 格式
print(result.content)
