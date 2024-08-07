import csv
from tkinter import*
import random

WP_color="#090c38"
T_color="#f8f400"
F_color="#cacbe2"
bagic_color="#ffffff"
text_color="white"

with open(r"C:\Users\user\Desktop\English-word-test\English-words.csv", encoding="UTF-8-sig") as file:
    questions=list(csv.reader(file))

answer=0

def next_question():
    global answer
    for i in range(4):
        buttons[i].config(bg=bagic_color)
    multi_choice=random.sample(questions, 4)
    answer=random.randint(0, 3)
    cur_question=multi_choice[answer][0]

    questions_label.config(text=cur_question)

    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])

def check_answer(idx):
    idx=int(idx)
    if answer==idx:
        buttons[idx].config(bg=T_color)
        window.after(54300, next_question)
    else:
        buttons[idx].config(bg=F_color)

window=Tk()
window.title("CO;DE 영어 단어 퀴즈 프로그램")
window.config(padx=30, pady=20, bg=WP_color)

questions_label=Label(window, width=22, height=2, text="test", font=("bold", 25), bg=WP_color, fg=text_color)
questions_label.pack()

buttons=[]
for i in range(4):
    btn=Button(window, text=f"{i}번", width=40, height=2, font=("bold", 15), command=lambda idx=i: check_answer(idx))
    btn.pack()
    buttons.append(btn)

next_btn=Button(window, text="다음 문제", width=15, height=2, font=("bold", 15), bg=T_color, command=next_question)
next_btn.pack(pady=30)

next_question()

window.mainloop()