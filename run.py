import pandas as pd
import gradio as gr


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


# 채팅 내역을 관리하는 클래스
class ChatHistory:
    def __init__(self):
        self.conversation = []  # 채팅 내역을 저장하는 리스트

    # 채팅 내역에 메시지를 추가하는 메소드
    def add_message(self, sender, message):
        self.conversation.append((sender, message))  # (발신자, 메시지) 튜플을 리스트에 추가

    # 현재까지의 채팅 내역을 문자열로 반환하는 메소드
    def get_conversation(self):
        return '\n'.join(f'{sender}: {message}' for sender, message in self.conversation)  # 각 채팅 메시지를 줄바꿈 문자로 연결

# 채팅 내역을 관리하는 인스턴스 생성
chat_history = ChatHistory()

# Gradio 인터페이스에서 호출될 함수
def chat(input_sentence):
    response = chatbot.find_best_answer(input_sentence)  # 입력된 문장에 대한 가장 좋은 답변을 찾음
    chat_history.add_message('You', input_sentence)  # 채팅 내역에 사용자의 메시지 추가
    chat_history.add_message('Chatbot', response)  # 채팅 내역에 챗봇의 응답 추가
    return chat_history.get_conversation()  # 현재까지의 채팅 내역을 반환

# 챗봇을 초기화하고 학습 데이터를 불러옴
filepath = 'ChatbotData.csv'
chatbot = LevenshteinChatBot(filepath)

# Gradio 인터페이스를 설정하고 실행
iface = gr.Interface(fn=chat, inputs=gr.inputs.Textbox(lines=2), outputs=gr.outputs.Textbox())
iface.launch()
