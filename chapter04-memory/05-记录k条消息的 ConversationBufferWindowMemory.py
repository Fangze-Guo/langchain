from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=2, return_messages=True)

memory.save_context({"input": "你好，我叫小明，是一名程序员"}, {"output": "你好，小明，很高兴认识你。"})
memory.save_context({"input": "我叫什么名字，是什么职业呢？"}, {"output": "你叫小明，是一名程序员。"})
memory.save_context({"input": "你是谁？"}, {"output": "我是AI"})

print(memory.load_memory_variables({}))