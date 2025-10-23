from langchain_core.prompts import ChatPromptTemplate

# 创建对话模板
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}"),
    ("user", "{question}"),
    ("assistant", "{example_answer}"),
    ("user", "{actual_question}")
])

# 格式化
messages = chat_prompt_template.format_messages(
    role="历史老师",
    question="中国有多少朝代？",
    example_answer="中国历史上有很多朝代...",
    actual_question="详细介绍唐朝"
) 

print(messages)