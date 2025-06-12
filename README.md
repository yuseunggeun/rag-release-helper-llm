# rag-release-helper-llm

**2025-1 졸업프로젝트**  
LLM에 대한 질의응답을 처리하는 서버입니다.

---

## 🛠 환경

- Python 3.12.4에서 정상 동작 확인
- LangChain 기반 RAG 아키텍처
- FastAPI 서버 구성

---

## 📦 종속성 설치

```bash
pip install -r requirements.txt
```

---

## 🔐 환경 변수 설정

`config.py`와 동일한 디렉토리에 `.env` 파일을 생성하여 다음 내용을 입력하세요:

```
OPENAI_API_KEY={당신의 openai api key}
PYDANTIC_V2_FORCE=1
CHROMA_DB_DIR={당신의 로컬 chroma_store 경로}
COLLECTION_NAME={chromaDB에서 사용할 컬렉션 이름}
```

---

## 🚀 서버 실행

```bash
python main.py
```

---

## 🌐 웹 인터페이스 접속

서버 실행 후, 브라우저에서 아래 주소로 접속하면 웹 기반 질의응답을 수행할 수 있습니다:

```
http://localhost:8000/chat/playground
```

---

## 📁 프로젝트 구조 예시

```
rag-release-helper-llm/
├── main.py
├── config.py
├── .env              # 환경 변수 파일 (직접 생성)
├── requirements.txt
└── ...
```

---

