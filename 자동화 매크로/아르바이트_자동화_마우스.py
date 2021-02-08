import os
import pyautogui
import pyperclip
import platform
import subprocess
import time


# 좌표 확인단
"""
time.sleep(5)
x, y = pyautogui.position()C:\\Users\\yoonjun\\Desktop\\알바\\제출\\출근

print(f'숨겨진 아이콘 표시 : {x, y}')
time.sleep(5)
x, y = pyautogui.position()
print(f'카카오톡 : {x, y}')
time.sleep(5)
x, y = pyautogui.position()

print(f'채팅방 위치 : {x, y}')
time.sleep(5)
x, y = pyautogui.position()
print(f'파일 전송 : {x, y}')
time.sleep(5)
x, y = pyautogui.position()
print(f'주소창 : {x, y}')
time.sleep(5)
x, y = pyautogui.position()
print(f'폴더 여백 : {x, y}')
"""

# 카카오톡 실행 및 채팅방 접속
def run_kakao():
    pyautogui.click(1679, 1062)
    pyautogui.doubleClick(1643, 1020)
    pyautogui.doubleClick(1790, 117)
    return True

# 카카오톡 지정 메시지 전송
def send_msg(arg):
    pyperclip.copy(arg)
    pyautogui.hotkey(cmd_key, 'v')
    pyautogui.press('enter')

# 출근
def start():
    direc = "C:\\Users\\yoonjun\\Desktop\\알바\\제출\\출근"
    msg = '안녕하세요~ 업무 시작하겠습니다!.'

    while True:
        time.sleep(3)
        ctime = time.strftime('%H:%M')

        if ctime == '22:11':
            kakao_st = run_kakao()
            if kakao_st:
                pyautogui.click(1291, 831)
                pyautogui.click(1462, 301)
                pyperclip.copy(direc)
                pyautogui.hotkey('ctrl','v')
                pyautogui.hotkey('enter')
                pyautogui.click(1426, 453)
                pyautogui.hotkey('ctrl','a')
                pyautogui.hotkey('alt','o')
                time.sleep(1)
                send_msg(msg)
                time.sleep(5)
                pyautogui.hotkey('esc')
                print('출근 완료')
                return True
                break
            
            else:
                continue

        else:
            print(f'출근 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# 오전 보고
def report_am():
    msg = '1200개 검수했습니다~'

    while True:
        time.sleep(3)
        ctime = time.strftime('%H:%M')

        if ctime == '22:04':
            run_kakao()
            send_msg(msg)
            pyautogui.hotkey('esc')
            print('오전 보고 완료')
            return True
            break

        else:
            print(f'오전 보고 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# Config changed by OS
cmd_key = 'ctrl'
home_key = ('home', '')
is_retina = False

if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)
    cmd_key = 'command'
    home_key = ('option', 'up')

pyautogui.PAUSE = 1

# 매크로 실행
if __name__ == "__main__":
    start = start()
    time.sleep(1)
    report_am = report_am()

    if start & report_am:
        exit(0)
        