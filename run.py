import pandas as pd
import gradio as gr

import pandas as pd


# 레벤슈타인 거리 계산 함수
def levenshtein_distance(s1, s2):
    # 긴 문자열이 s1에 오도록 재정렬
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # s2가 비어 있다면 s1의 길이를 반환
    if len(s2) == 0:
        return len(s1)

    # 행렬을 초기화
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]

        # 삽입, 삭제, 변경 비용을 비교
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 문자를 s1에 삽입
            deletions = current_row[j] + 1       # j 문자를 s1에서 삭제
            substitutions = previous_row[j] + (c1 != c2) # s1의 j 문자를 변경
            current_row.append(min(insertions, deletions, substitutions))

        previous_row = current_row

    return previous_row[-1]


class LevenshteinChatBot:
    def __init__(self, filepath):
        # 질문과 답변을 로드합니다.
        self.questions, self.answers = self.load_data(filepath)

    # 학습 데이터를 불러오는 함수
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문을 리스트로 저장
        answers = data['A'].tolist()    # 답변을 리스트로 저장
        return questions, answers

    # 입력 문장에 가장 잘 맞는 답변을 찾는 함수
    def find_best_answer(self, input_sentence):
        # 각 질문과의 레벤슈타인 거리를 계산합니다.
        distances = [levenshtein_distance(input_sentence, question) for question in self.questions]
        # 가장 거리가 짧은 질문을 찾습니다.
        best_match_index = distances.index(min(distances))
        # 해당 질문의 답변을 반환합니다.
        return self.answers[best_match_index]


def chat(input_sentence):
    response = chatbot.find_best_answer(input_sentence)
    return response

# CSV 파일 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 레벤슈타인 챗봇 인스턴스를 생성합니다.
chatbot = LevenshteinChatBot(filepath)

# Gradio 인터페이스를 정의하고 실행합니다.
iface = gr.Interface(fn=chat, inputs="text", outputs="text")
iface.launch()
