import os

import dotenv
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

chat_prompt_template_A = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个精通各个领域知识的知名教授"),
        ("human", "请你先尽可能详细的解释一下：{knowledge}，并且{action}"),
    ]
)

chain_A = LLMChain(
    llm=chat_model,
    prompt=chat_prompt_template_A,
    verbose=True,
    output_key="chain_A_output",
)

chat_prompt_template_B = ChatPromptTemplate.from_messages(
    [
        ("system", "你非常善于提取文本中的重要信息，并作出简短的总结"),
        ("human", "这是一段完整的解释说明内容：{chain_A_output}"),
        ("human", "根据上述说明，请简短的总结出简明扼要的内容来。"),
    ]
)

chain_B = LLMChain(
    llm=chat_model,
    prompt=chat_prompt_template_B,
    verbose=True,
    output_key="chain_B_output",
)

sequential_chain = SequentialChain(
    chains=[chain_A, chain_B],
    verbose=True,
    input_variables=["knowledge", "action"],
    output_variables=["chain_A_output", "chain_B_output"],
)

result = sequential_chain.invoke({
    "knowledge": "为什么LLM是当今的热点",
    "action": "举一个实际例子",
})
print(result)
