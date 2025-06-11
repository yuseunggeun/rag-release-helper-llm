from fastapi import FastAPI
from langserve import add_routes
from chain.rag_chain import rag_chain

# FastAPI 앱 + LangServe 연결
app = FastAPI()
add_routes(app, rag_chain, path="/chat")


@app.get("/")
def root():
    return {"message": "LLM server and LangServe is running on port 8100"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True)
