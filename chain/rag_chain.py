from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableBranch
from langchain_core.runnables import RunnablePick
from langchain_openai import ChatOpenAI
from retriever.retriever import Retriever  # 벡터 검색 retriever
from config import OPENAI_API_KEY

# LLM 설정
llm = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=OPENAI_API_KEY)

# RAG 체인 설정
prompt = ChatPromptTemplate.from_template("""
당신은 오픈소스 프로젝트에 대한 질문에 답하는 전문가입니다.
아래는 해당 github repository에서 검색된 내용입니다:

{context}

위 내용을 바탕으로 질문에 답해주세요.

질문: {question}
""")

simple_prompt = ChatPromptTemplate.from_template("""
당신은 오픈소스 프로젝트에 대한 질문에 답하는 전문가입니다. 
질문에 답해주세요.

질문: {question}
""")


# 질문 분기 처리
def use_simple_chain(input: dict) -> bool:
    return input.get("use_rag", 1) == 0


def return_true(_):
    return True


# 문서 내용 문자열로 병합
def combine_docs(doc_list):
    if not isinstance(doc_list, list):
        return "리스트 형식의 문서가 아닙니다."
    if not doc_list:
        return "검색된 문서가 없습니다."
    return "\n\n".join(doc.page_content for doc in doc_list)


# 질문 추출
extract_question = RunnableMap({"question": RunnablePick("question")})

retriever = Retriever(default_k=3)  # 기본 검색 개수는 3개로 설정

# db에서 문서 검색
retrieve_docs = RunnableMap({
    "context": retriever,
    "question": RunnablePick("question")
})

# RAG 체인에서 사용할 문서와 질문 포맷팅
format_context = RunnableMap({
    "context": RunnablePick("context") | combine_docs,
    "question": RunnablePick("question")
})

# 전체 체인 연결
rag_chain = (extract_question | retrieve_docs | format_context | prompt | llm)

# 단순 질문에 대한 답변 체인 연결(RAG 미사용)
simple_chain = (extract_question | simple_prompt | llm)

# use_rag가 0인 경우에만 simple_chain로 분기하는 체인 설정
branching_chain = RunnableBranch((use_simple_chain, simple_chain),
                                 (return_true, rag_chain), rag_chain)
