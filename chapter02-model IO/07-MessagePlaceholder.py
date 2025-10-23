from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手，名字叫{name}"),
        # 当消息不确定时，使用 MessagesPlaceholder 占位，也可作为历史消息使用
        MessagesPlaceholder(variable_name="msgs"),
    ]
)

response = chat_prompt_template.invoke(
    {"name": "小明", "msgs": [HumanMessage(content="1+1=?"), AIMessage(content="2")]}
)

print(response)

"""输出：
messages=[
SystemMessage(content='你是一个AI助手，名字叫小明', additional_kwargs={}, response_metadata={}), 
HumanMessage(content='1+1=?', additional_kwargs={}, response_metadata={}),
AIMessage(content='2', additional_kwargs={}, response_metadata={})]
"""
