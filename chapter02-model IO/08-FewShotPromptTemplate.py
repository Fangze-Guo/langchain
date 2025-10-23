import os

import dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

# 示例提示词模板
example_prompt = PromptTemplate.from_template(template="输入：{input}\n输出：{output}")

# 示例列表
examples = [
    {"input": "1+1=?", "output": "2"},
    {"input": "2+2=?", "output": "4"},
    {"input": "3+3=?", "output": "6"},
]

# 少样本提示词模板
few_shot_prompt_template = FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    # 后缀提示词
    suffix="输入：{input}\n输出：",
    # 输入变量
    input_variables=["input"],
)

result = few_shot_prompt_template.invoke(input={"input": "4+4=?"})
print(result.to_string(), end="")

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

response = chat_model.invoke(result)
print(response.content)

"""
输入：1+1=?
输出：2

输入：2+2=?
输出：4

输入：3+3=?
输出：6

输入：4+4=?
输出：8
"""
