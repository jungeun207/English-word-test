import csv #CSV 파일을 읽기 위한 모듈
from tkinter import* #TKinter 모듈을 사용하여 GUI를 만들기 위한 import
import random #단어를 랜덤하게 나타내기 위한 모듈

WP_color="배경 색깔"
T_color="정답일 때 버튼 색깔"
F_color="오답일 때 버튼 색깔"
bagic_color="기본 버튼 색깔"
text_color="영어 단어 색깔"

#CSV 파일에서 데이터를 읽어오기
with open(r"파일 경로", encoding="UTF-8-sig") as file:
    questions=list(csv.reader(file)) #CSV 파일을 읽어서 리스트로 저장

answer=0 #정답의 인덱스를 저장하는 변수

def next_question():
    '''
    다음 문제를 표시하고, 버튼을 랜덤으로 설정한다.
    '''
    global answer
    #모든 버튼의 배경색을 기본 색상으로 초기화
    for i in range(4):
        buttons[i].config(bg=bagic_color)
    #질문을 랜덤하게 4개 선택
    multi_choice=random.sample(questions, 4)
    #정답의 인덱스를 랜덤하게 설정
    answer=random.randint(0, 3)
    #현재 질문을 설정
    cur_question=multi_choice[answer][0]
    questions_label.config(text=cur_question) #레이블에 질문 표시

    #버튼에 답을 설정
    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])

def check_answer(idx):
    '''
    사용자가 선택한 답을 확인하고 정답 여부에 따라 버튼 색상을 변경한다.
    '''
    idx=int(idx) #선택한 버튼의 인덱스를 정수로 변환
    if answer==idx: #정답일 경우
        buttons[idx].config(bg=T_color) #버튼 색상을 정답 색으로 변경
        window.after(100, next_question) #10ms 후에 다음 문제를 표시
    else: #오답일 경우
        buttons[idx].config(bg=F_color) #버튼 색상을 오답 색으로 변경

#TKinter 윈도우 생성
window=Tk()
window.title("CO;DE 영어 단어 퀴즈 프로그램") #윈도우 제목 설정
window.config(padx=30, pady=20, bg=WP_color) #윈도우 여백 및 배경 색상 설정

#질문 레이블 생성 및 설정
questions_label=Label(window, width=22, height=2, text="test", font=("bold", 25), bg=WP_color, fg=text_color)
questions_label.pack() #레이블 윈도우에 추가

#버튼을 생성하고 설정
buttons=[]
for i in range(4):
    btn=Button(window, text=f"{i}번", width=40, height=2, font=("bold", 15), command=lambda idx=i: check_answer(idx))
    btn.pack() #버튼을 윈도우에 추가
    buttons.append(btn) #버튼을 리스트에 추가

#'다음 문제' 버튼 생성 및 설정
next_btn=Button(window, text="다음 문제", width=15, height=2, font=("bold", 15), bg=T_color, command=next_question)
next_btn.pack(pady=30) #버튼을 윈도우에 추가

#첫 번째 문제를 표시
next_question()

#TKinter 윈도우를 활성화 상태로 유지
window.mainloop()
