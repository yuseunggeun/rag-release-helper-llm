from langchain_core.runnables import Runnable
from langchain_core.documents import Document
from vectorstore.db import vectorstore
import logging

# 로깅 설정
logger = logging.getLogger(__name__)


class Retriever(Runnable):

    # 기본 검색 문서 개수는 3개로 설정
    def __init__(self, default_k=3):
        self.default_k = default_k
        self.retriever = vectorstore.as_retriever(
            search_kwargs={"k": default_k})

    def invoke(self, input: dict, config=None):
        try:
            question = input.get("question", "")
            #k = input.get("k", self.default_k)
            #self.retriever.search_kwargs["k"] = k

            # 벡터 서치 실행
            docs = self.retriever.get_relevant_documents(question)

            if not docs:
                logger.info(f"[Retriever] No documents found for: {question}")
                return [Document(page_content="관련 문서를 찾지 못했습니다.")]
            return docs

        # 오류 발생시
        except Exception as e:
            logger.warning(f"[Retriever] Error during retrieval: {e}")
            return [Document(page_content="문서 검색 중 오류가 발생했습니다.")]
