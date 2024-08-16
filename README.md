[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yoHXt_g5)
# 프로젝트 이름
- 의료법 및 관련 판례 QA Engine
<br>

## 프로젝트 소개
<예시 1>
- 이 프로젝트는 증권 배당 데이터와 관련된 정보를 효율적으로 관리하고, 관련 세법에 대한 질문과 답변을 제공하는 QA(Question-Answering) 엔진을 구축하는 것입니다.
- 사용자는 이 엔진을 통해 특정 기업의 배당 정보나 세법 관련 질문에 대한 답변을 신속하게 얻을 수 있습니다.
<br>

## 팀원 구성

<div align="center">

| **팀장** | **팀원 1** | **팀원 2** | **팀원 3** |
| :------: |  :------: | :------: | :------: |
|[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> 박현애](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> 박동재](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> 진주영](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> 김동호](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> ](https://github.com/) |
</div>

<br>

## 1. 개발 환경

- 주 언어 : Python
- 버전 및 이슈관리 : 3.10
- 협업 툴 : notion, git, slack

<br>

## 2. 채택한 개발 기술과 브랜치 전략

### PyPDFLoader, Chroma, UpstageEmbeddings, ChatUpstage ~~

- PyPDFLoader
  - **PyPDFLoader**는 **LangChain** 프레임워크에서 제공하는 PyPDFLoader 모듈을 import하는 코드입니다. 이 모듈은 PDF 파일에서 텍스트 데이터를 추출하는데 사용됩니다.
    <br>
    <br>
    **PyPDFLoader의 주요 기능**
      1. PDF 문서 로딩: PyPDFLoader는 PDF 파일을 읽고, 그 안에 포함된 텍스트를 추출하여 사용할 수 있도록 변환합니다.
      2. 텍스트 추출: PDF 문서에서 페이지별로 텍스트를 효과적으로 추출할 수 있습니다. 이를 통해 문서의 내용을 쉽게 분석하거나 처리할 수 있습니다.
      3. 문서 처리 파이프라인 통합: PyPDFLoader는 LangChain의 다른 모듈과 통합하여, 다양한 자연어 처리(NLP) 작업을 수행할 수 있는 파이프라인의 일환으로 사용될 수 있습니다.

- Chroma
  - **Chroma**는 PyPDFLoader와 마찬가지로 **LangChain** 프레임워크에서 제공하는 모듈을 import하는 코드입니다. **Chroma**는 주로 임베딩(embedding)과 검색 관련 작업을 수행하는 벡터 데이터베이스(Vector Database)입니다. LangChain 프레임워크에서 Chroma는 벡터 임베딩을 저장하고, 주어진 쿼리에 대해 가장 유사한 문서나 데이터를 검색하는데 사용됩니다.
    <br>
    <br>
    **Chroma 주요 기능**
      1. 임베딩 저장소: 텍스트 데이터를 벡터로 변환하여 저장할 수 있습니다. 이 벡터는 나중에 유사한 텍스트를 검색하는데 사용됩니다.
      2. 유사도 검색: Chroma는 벡터 간의 유사성을 계산하여 특정 쿼리와 가장 유사한 데이터 포인트를 빠르게 찾아낼 수 있습니다.
      3. 확장성: 대량의 데이터를 처리할 수 있는 기능을 갖추고 있어, 다양한 규모의 프로젝트에서 유용하게 사용될 수 있습니다.
      4. 통합 가능성: LangChain의 다른 모듈과 함께 사용하여 복잡한 자연어 처리 파이프라인을 구성할 수 있습니다.
   
- UpstageEmbeddings
  - **UpstageEmbeddings**는 Upstage에서 제공하는 라이브러리입니다. Upstage는 한국어와 같은 저자원 언어에 특화된 AI 모델을 개발하는 회사로, UpstageEmbeddings는 이 회사의 임베딩 모델을 LangChain에서 사용할 수 있도록 지원합니다.
    <br>
    <br>
    **UpstageEmbeddings 주요 기능**
      1. 임베딩 생성: 텍스트 데이터를 고차원 벡터로 변환하여 기계 학습 모델이나 검색 시스템에서 사용할 수 있도록 합니다.
      2. 유사도 계산: 생성된 임베딩을 사용하여 텍스트 간의 유사성을 평가할 수 있습니다. 이는 추천 시스템이나 검색 엔진에 유용합니다.
      3. 다양한 NLP 작업 지원: UpstageEmbeddings는 문서 분류, 클러스터링, 질문 응답 등의 다양한 자연어 처리 작업에 활용될 수 있습니다.
      4. 모델 통합: UpstageEmbeddings는 LangChain의 다른 모듈과 쉽게 통합되어, 복잡한 NLP 파이프라인을 구축하는데 도움을 줍니다.

### Beautifulsoup, Selenium

- Beautifulsoup
  - 네이버 증권 페이지에서 배당률, 주가 등의 정보를 포함한 HTML 테이블에서 데이터를 추출합니다.

- Selenium
  - 웹 페이지에서 동적 콘텐츠를 로드합니다.
  - 특정 종목의 배당 데이터를 얻기 위해 종목 검색 후, 관련 페이지로 이동해야 할 때, 이 과정을 자동화합니다. 

### 브랜치전략 
    
- 브랜치 전략
  - Git-flow 전략을 기반으로 main, develop 브랜치와 feature 보조 브랜치를 운용했습니다.
  - main, develop, Feat 브랜치로 나누어 개발을 하였습니다.
    - **main** 브랜치는 배포 단계에서만 사용하는 브랜치입니다.
    - **develop** 브랜치는 개발 단계에서 git-flow의 master 역할을 하는 브랜치입니다.
    - **Feat** 브랜치는 기능 단위로 독립적인 개발 환경을 위하여 사용하고 merge 후 각 브랜치를 삭제해주었습니다.


<br>

## 3. 프로젝트 구조
```
├── README.md
├── .gitignore
└── src
     ├── App.py
     ├── index.py
     ├── api
     │     └── GoogleAPI.jsx
     └── styles
           └── Globalstyled.jsx
...

```

<br>

## 4. 역할 분담

### 팀원 1
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 2
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 3
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

## 5. 개발 기간 및 작업 관리

### 개발 기간
- 전체 개발 기간 : 2024-08-13 ~ 2024-08-18
- 기능 구현 : 2024-08-15 ~ 2024-08-18
- 그외 기간 작성
  
<br>

### 작업 관리
<예시>

- 아래와 같은 오류가 발생했습니다.

```python
C:\Users\yong\AppData\Local\Programs\Python\Python311\Lib\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.llms.openai.OpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAI`.
  warn_deprecated(
```

### 설명

- langchain_community.llms.openai.OpenAI는 langchain-community 0.0.10에서 deprecate되었으며 0.2.0에서 제거될 예정입니다.
- 업데이트된 버전의 클래스가 langchain-openai 패키지에 있으며 이것을 사용해야 합니다.


### 해결

- 명령 프롬프트(또는 터미널)에서 다음 명령을 실행해 langchain-openai 패키지를 설치합니다.

```python
pip install -U langchain-openai
```

- 아래와 같이 import문 변경하면 해결됩니다.
```python
from langchain_openai import OpenAI
```


<br>

## 5. 프로젝트 후기

### 팀원 1
프로젝트 후기 작성

### 팀원 2
프로젝트 후기 작성
<br>

