import time
from datetime import datetime, timedelta
import tkinter.messagebox as msgbox
from tkinter import *
import pyautogui

# 함수부_Tk에서 사용될 함수는 Tk 이전에 선언되어야 함.
def btncmd() :
    nyam = ent.get() # ent 엔트리 객체의 내용을 가져오라는 의미.
    nyam = int(nyam)
    ctime = datetime.now() # 시작 당시 시각.
    qtime = ctime + timedelta(minutes=nyam) # 알람 예정 시각.
    qtime = qtime.strftime("%H:%M")
    
    while True :
        time.sleep(10)
        ftime = time.strftime("%H:%M") # 현재 시각.
        if ftime == qtime :
            pyautogui.hotkey('win','d') # 바탕화면 이동.
            time.sleep(1)
            msgbox.showinfo("Alarm", "Just get some rest") # 알람창 띄우기.
            break

# GUI 설정부

root = Tk() # Tk() 선언.
root.title("Get some rest!") # 윈도우 제목 기입.
root.geometry("500x300+700+350") # 윈도우 크기 & 출력 좌표 지정.
root.resizable(False, False) # 창 크기 고정.

ent = Entry(root, width =50)
ent.pack()
ent.insert(0, "Please type only numbers(minutes) here.")

btn1 = Button(root, width=10, height=3, text="Start", command=btncmd) # (객체, 가로 크기, 세로 크기, 버튼 텍스트, 실행 함수)
'''
btn1 = Button(root, padx=30, pady=10, text="Start")
             (객체, x패딩, y패딩, 버튼 텍스트)
'''
btn1.pack() # pack() 함수를 사용하여 객체에 포함.

label1 = Label(root, text="yrohh.tistory.com") # 여백에 텍스트만 입력.
label1.pack(side="bottom", anchor="e")

root.mainloop() # 실행부.

# 참고 블로그 : https://m.blog.naver.com/amethyst_lee/222011409761