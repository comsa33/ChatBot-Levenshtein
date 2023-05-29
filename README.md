# Levenshtein Chatbot

이 프로젝트는 레벤슈타인 거리 알고리즘을 이용하여 만든 간단한 챗봇입니다. 사용자가 질문을 입력하면, 챗봇은 사전에 정의된 질문 중 가장 유사한 질문을 찾아 그에 해당하는 답변을 제공합니다.

- 학습 데이터 셋 출처: (https://github.com/songys/Chatbot_data)

## 사용 방법

1. 이 리포지토리를 클론합니다.

    ```bash
    git clone https://github.com/comsa33/ChatBot-Levenshtein.git
    ```

2. 클론한 디렉토리로 이동합니다.

    ```bash
    cd ChatBot-Levenshtein
    ```

3. 필요한 패키지를 설치합니다.

    ```bash
    pip install gradio pandas
    ```

4. 챗봇을 실행합니다.

    ```bash
    python run.py
    ```

5. 출력된 URL을 웹 브라우저에 붙여넣습니다. 그런 다음 챗봇에게 원하는 질문을 입력하면, 챗봇이 대답을 제공합니다.

## 주의 사항

이 챗봇은 간단한 데모를 위한 것이므로, 복잡한 질문에 대한 답변을 제공하기에는 한계가 있습니다.

## 기여

기여는 언제나 환영합니다. 이슈를 제기하거나 풀 리퀘스트를 보내 주세요.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
