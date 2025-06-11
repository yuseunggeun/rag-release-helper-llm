from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=OPENAI_API_KEY)

prompt = ChatPromptTemplate.from_template("""

질문: {question}
""")

rag_chain = prompt | llm
