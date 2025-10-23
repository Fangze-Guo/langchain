import os

import dotenv
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

# 定义列表解析器
output_parser = CommaSeparatedListOutputParser()

# 提示词模板
prompt_template = PromptTemplate.from_template(
    template="生成5个关于{text}的列表. {format_instructions}",
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
print("prompt_template:", prompt_template.format(text="示例"))

chain = prompt_template | chat_model | output_parser

result = chain.invoke(input={"text": "心情"})
print("result:", result)
