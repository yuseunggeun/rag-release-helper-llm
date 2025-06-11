from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os

load_dotenv()

# 사용할 llm 설정
llm = ChatOpenAI(model="gpt-4o",
                 temperature=0.7,
                 api_key=os.getenv("OPENAI_API_KEY"))

# LangChain 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages([("system",
                                            "당신은 오픈소스 관련 질문을 답변하는 AI입니다."),
                                           ("human", "{question}")])

chat_chain = prompt | llm

# FastAPI 앱 + LangServe 연결
app = FastAPI()
add_routes(app, chat_chain, path="/chat")


@app.get("/")
def root():
    return {"message": "LLM server and LangServe is running on port 8100"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
