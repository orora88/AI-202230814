import pandas as pd

# 레벤슈타인 거리 계산 함수 불러오기
from lv_distance import cal_distance

# 챗봇 클래스를 정의
class SimpleChatBot:
    # 챗봇 객체를 초기화하는 메서드, 초기화 시에는 입력된 데이터 파일을 로드함
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)
        
    
    # CSV 파일로부터 질문과 답변 데이터를 불러오는 메서드
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    # 입력 문장에 가장 잘 맞는 답변을 찾는 메서드, 입력 문장을 기존 질문리스트와 비교하여 가장 작은 거리를 가진 질문의 답변을 반환함
    def find_best_answer(self, input_sentence):
        #사용자 입력 문장과 기존 질문들 간의 레벤슈타인 거리를 계산하고 가장 거리가 작은 질문의 인덱스를 찾음
        distance = [cal_distance(input_sentence, i) for i in self.questions]
        best_match_index = distance.index(min(distance))
        # 가장 유사한 질문에 해당하는 답변을 반환
        return self.answers[best_match_index]

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
