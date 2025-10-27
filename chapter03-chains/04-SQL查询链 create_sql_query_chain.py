import os

import dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains.sql_database.query import create_sql_query_chain

db_user = "root"
db_password = "123456"
db_host = "localhost"
db_port = 3306
db_name = "lingtu_picture"

db = SQLDatabase.from_uri(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

print(db.dialect)

print(db.get_usable_table_names())

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DEEPSEEK_BASE_URL")

chat_model = ChatOpenAI(
    model="deepseek-chat",
)

chain = create_sql_query_chain(llm=chat_model, db=db)
result = chain.invoke({"question": "查询所有用户"})
print(result)   # SQLQuery: SELECT `id`, `userAccount`, `userName`, `userRole`, `createTime` FROM `user` WHERE `isDelete` = 0 LIMIT 5
