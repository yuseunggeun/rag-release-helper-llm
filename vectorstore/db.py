from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY, CHROMA_DB_DIR

# 임베딩 모델이 저장할 때와 같아야 제대로 검색 가능
embedding = OpenAIEmbeddings(model="text-embedding-3-small",
                             openai_api_key=OPENAI_API_KEY)

# ChromaDB에 연결
vectorstore = Chroma(collection_name="github_docs",
                     embedding_function=embedding,
                     persist_directory=CHROMA_DB_DIR)

# 벡터서치를 위한 retriever 설정
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
