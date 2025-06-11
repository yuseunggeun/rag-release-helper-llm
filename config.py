from dotenv import load_dotenv
import os

load_dotenv()

# 환경변수 로드
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "github_docs")
