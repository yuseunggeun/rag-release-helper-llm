from fastapi import FastAPI
from langserve import add_routes
from chain.rag_chain import branching_chain
from pydantic import BaseModel
import json
# FastAPI 앱 + LangServe 연결
app = FastAPI()


@app.middleware("http")
async def log_request_body(request, call_next):
    body = await request.body()
    try:
        json_body = json.loads(body)
        print(f"Request body: {json_body}")
    except json.JSONDecodeError:
        print(f"Request body is not valid JSON: {body}")
    response = await call_next(request)
    return response


class ChatInput(BaseModel):
    question: str
    use_rag: int = 1


add_routes(app, branching_chain, path="/chat", input_type=ChatInput)
'''
@app.get("/")
def root():
    return {"message": "LLM server and LangServe is running on port 8100"}
'''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
