from fastapi import FastAPI
from langserve import add_routes
from chain.rag_chain import branching_chain
from pydantic import BaseModel
import json
# FastAPI 앱 + LangServe 연결
app = FastAPI()


# request body 로깅용 미들웨어
@app.middleware("http")
async def log_request_body(request, call_next):
    body = await request.body()
    try:
        json_body = json.loads(body)  # JSON이 아닌 경우 예외 발생
        print(f"Request body: {json_body}")
    except json.JSONDecodeError:
        print(f"Request body is not valid JSON: {body}")
    response = await call_next(request)
    return response


# 입력 스키마 정의
class ChatInput(BaseModel):
    question: str
    use_rag: int = 1


# LangServe에 라우트 추가
add_routes(app, branching_chain, path="/chat", input_type=ChatInput)
'''
@app.get("/")
def root():
    return {"message": "LLM server and LangServe is running on port 8100"}
'''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
