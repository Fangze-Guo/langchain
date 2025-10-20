# 示例列表
import os

import dotenv
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

examples = [
    {"input": "2🦜2", "output": "4"},
    {"input": "2🦜3", "output": "8"},
]

# 示例提示词模板
example_prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}是多少？"), ("ai", "是{output}")]
)

# 定义少样本提示词模板
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt, examples=examples
)

# 完整提示词模板
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个计算专家"),
        few_shot_prompt,
        ("human", "{input}是多少？"),
    ]
)

print(final_prompt.invoke({"input": "2🦜4"}).to_string())

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

response = chat_model.invoke(final_prompt.invoke({"input": "2🦜4"}))
print(response.content)


"""
System: 你是一个计算专家
Human: 2🦜2是多少？
AI: 是4
Human: 2🦜3是多少？
AI: 是8
Human: 2🦜4是多少？
是16
"""