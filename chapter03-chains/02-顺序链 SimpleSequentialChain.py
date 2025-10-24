import os

import dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

chat_prompt_template_A = ChatPromptTemplate.from_messages(
    [("system", "你是一个历史专家"), ("human", "解释一下{input}背后的历史故事。")]
)

chain_A = LLMChain(
    llm=chat_model,
    prompt=chat_prompt_template_A,
    verbose=True,  # 打印详细日志信息
)

chat_prompt_template_B = ChatPromptTemplate.from_messages(
    [
        ("system", "你非常善于提取文本中的重要信息，并作出简短的总结"),
        ("human", "这是一段完整的解释说明内容：{description}"),
        ("human", "根据上述说明，请简短的总结出简明扼要的内容来。"),
    ]
)


chain_B = LLMChain(
    llm=chat_model,
    prompt=chat_prompt_template_B,
    verbose=True,
)

sequential_chain = SimpleSequentialChain(
    chains=[chain_A, chain_B],
    verbose=True,
)
# 针对 SimepleSequentialChain，唯一的输入变量名是 input
# 第一个链的输出，会作为第二个链的输入
# 第二个链的输出，会作为最终的输出
result = sequential_chain.invoke(input={"input": "条条大路通罗马"})
print(result)
