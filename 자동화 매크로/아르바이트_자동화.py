'''
# 출근 08:56

1. 시간이 되면 카카오톡 실행
2. 맨 위 채팅방 입장
3. (출근 복사 폴더 디렉토리)
4. 출근 텍스트 보내기

# 오전보고 10:58

1. 시간이 되면 카카오톡 실행
2. 맨 위 채팅방 입장
3. 텍스트 보내기


# 중간보고 14:58

1. 시간이 되면 카카오톡 실행
2. 맨 위 채팅방 입장
3. 텍스트 보내기

# 퇴근 17:56

1. 시간이 되면 카카오톡 실행
2. 맨 위 채팅방 입장
3. (퇴근 복사 폴더 디렉토리)
4. 퇴근 텍스트 보내기
'''

import os
import pyautogui
import pyperclip
import platform
import subprocess
import time

# pyautogi 딜레이 설정 및 현재 파일 절대경로로 현재 디렉토리 수정
def initialize():
    print(pyautogui.size())
    pyautogui.PAUSE = 0.5
    python_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(python_path)

# 운영체제별 카카오톡 주소 저장
def get_kakao_cmd():
    user_os = platform.system()
    kakao_path = ['C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe']
    if user_os == 'Darwin':
        kakao_path = ['open', '-a', 'KakaoTalk']
    return kakao_path

# 카카오톡 실행
def run_kakao():
    kakao_path = get_kakao_cmd()
    print(f'Run KakaoTalk : {kakao_path}')
    try:
        subprocess.run(kakao_path)
    except Exception:
        print('[ERROR] Execute Kakaotalk')
        raise

# 카카오톡 지정 채팅방 입장
def enter_chatroom(chat_idx):
    # Focus on 1st chatroom
    pyautogui.hotkey(*home_key)
    print(*home_key)
    print(f"Enter the {chat_idx}th chatroom")
    for _ in range(1, chat_idx):
        pyautogui.press('down')
    pyautogui.press('enter')

# 카카오톡 지정 메시지 전송
def send_msg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey(cmd_key, 'v')
    pyautogui.press('enter')

# 출근 함수
def start():
    initialize()
    chatroom_idx = 1
    direc = "C:\\Users\\yoonjun\\Desktop\\알바\\제출\\출근"
    my_msg = '안녕하세요~ 업무 시작하겠습니다!'
    while True:
        time.sleep(10)
        ctime = time.strftime('%H:%M')
        if ctime == '08:57':
            run_kakao()
            time.sleep(3)
            enter_chatroom(chatroom_idx)
            pyautogui.hotkey('ctrl','t')
            pyautogui.hotkey('fn','f4')
            pyautogui.hotkey('ctrl','a')
            pyperclip.copy(direc)
            pyautogui.hotkey('ctrl','v')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('alt','o')
            time.sleep(1)
            send_msg(my_msg)
            time.sleep(7)
            pyautogui.hotkey('esc')
            print('출근 완료')
            return True
            break
        else :
            print(f'출근 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# 오전 보고 함수
def report_am():
    initialize()
    chatroom_idx = 1
    my_msg = '1000개 검수했습니다!'
    while True:
        time.sleep(10)
        ctime = time.strftime('%H:%M')
        if ctime == '10:57': 
            run_kakao()
            time.sleep(3)
            enter_chatroom(chatroom_idx)
            send_msg(my_msg)
            time.sleep(7)
            pyautogui.press('esc')
            print('오전 보고 완료')           
            return True
            break
        else :
            print(f'오전 보고 매크로 실행 예정입니다. 현재 시각 : {ctime}')

# 오후 보고 함수
def report_pm():
    initialize()
    chatroom_idx = 1
    my_msg = '3000개 검수했습니다!'
    while True:
        time.sleep(10)
        ctime = time.strftime('%H:%M')
        if ctime == '14:58': 
            run_kakao()
            time.sleep(3)
            enter_chatroom(chatroom_idx)
            send_msg(my_msg)
            time.sleep(7)
            pyautogui.press('esc')
            print('오후 보고 완료')           
            return True
            break
        else :
            print(f'오후 보고 매크로 예정입니다. 현재 시각 : {ctime}')

# 퇴근 함수_2일부터 ㅈㅎ에게 보내야 하므로 매크로 필요 없음.
'''
def leave():
    initialize()
    chatroom_idx = 1
    direc = "C:\\Users\\yoonjun\\Desktop\\알바\\제출\\2일"
    my_msg = '오늘도 고생 많으셨습니다!'
    while True:
        time.sleep(5)
        ctime = time.strftime('%H:%M')
        if ctime == '23:45':
            run_kakao()
            time.sleep(1)
            enter_chatroom(chatroom_idx)
            pyautogui.hotkey('ctrl','t')
            pyautogui.hotkey('fn','f4')
            pyautogui.hotkey('ctrl','a')
            pyperclip.copy(direc)
            pyautogui.hotkey('ctrl','v')
            pyautogui.hotkey('enter')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('alt','o')
            time.sleep(1)
            send_msg(my_msg)
            time.sleep(10)
            pyautogui.hotkey('esc')
            print('퇴근 완료')
            return True
            break
        else :
            print(f'퇴근 매크로 실행 예정입니다. 현재 시각 : {ctime}')
'''




# Config changed by OS
cmd_key = 'ctrl'
home_key = ('home', '')
is_retina = False

if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)
    cmd_key = 'command'
    home_key = ('option', 'up')

# 매크로 실행
if __name__ == "__main__":
    start = start()
    report_am = report_am()
    report_pm = report_pm()
    # leave = leave()
    if start & report_am & report_pm:
        exit(0)

# 참고 출처 : https://shine-yeolmae.tistory.com/52