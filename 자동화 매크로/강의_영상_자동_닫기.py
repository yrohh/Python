import os
import pyautogui
import pyperclip
import platform
import subprocess
import time
from datetime import datetime, timedelta


# 학습종료 위치 1860, 80

# 종료 실행 함수
def quit_check() :
    
    while True:
        time.sleep(3)
        ftime = time.strftime("%H:%M") # 현재 시간을 00시 00분 형식의 문자열로 변환
        print(f'현재 시간은 {ftime}입니당~')
        if ftime == qtime : # 현재 시간이 종료 예약 시간과 일치할 경우
            pyautogui.click(1860, 80) # 1860, 80 지점을 클릭
            return True # quit_check 에 True 반환
            break # while문 종료

# 매크로 실행부
if __name__ == "__main__":
    ctime = datetime.now() # 스크립트 실행 시간
    qtime = ctime + timedelta(minutes=1) # n분 후 종료 예약 시간
    qtime = qtime.strftime("%H:%M") # 00시 00분 형식의 문자열로 변환
    print(f'종료 예정 시간은 {qtime}입니당~')
    quit_check = quit_check()

    if quit_check :
        exit(0)