import pyautogui
import time
from datetime import datetime, timedelta


# 학습종료 위치 1860, 80

def takeaclass(x, y, times) :
    ctime = datetime.now() # 현재 시간 불러오기. 시간 계산을 위해서 datetime 라이브러리 사용.
    qtime = ctime + timedelta(minutes=times) # 현재 시간에 n분 만큼 더하기.
    qtime = qtime.strftime("%H:%M") # 더한 시간 -> 종료 시간.
    print(f'종료 예정 시간은 {qtime}입니다.')
    pyautogui.hotkey('fn','pgdn') # 수업 듣기 버튼 클릭을 위한 페이지 내림.
    pyautogui.click(x, y) # 교시별 학습 버튼 클릭.
    pyautogui.hotkey('win','right') # 영상 오른쪽 전환.
    pyautogui.hotkey('enter') # 이어서 보기 창 내림.
    pyautogui.click(1330, 400) # 영상 재생.

    while True:
        # time.sleep(3)
        ftime = time.strftime("%H:%M") # 현재 시간 불러오기.
        print(f'현재 시간은 {ftime}입니다.')
        if ftime == qtime : # 현재 시간과 종료 시간이 일치할 경우 종료.
            pyautogui.click(1860, 80) # 학습 완료 버튼 클릭.
            return True


pyautogui.PAUSE=2.5 # 모든 pyautogui에 딜레이를 주어 누락 예방.

# 매크로 실행부
if __name__ == "__main__":
    pyautogui.click(500,400)
    # first_class = takeaclass(620, 142, 20)
    second_class = takeaclass(620, 238, 30)
    third_class = takeaclass(620, 334, 35)
    fourth_class = takeaclass(620, 435, 37)

    pyautogui.click(80, 300) # 강의 선택.
    pyautogui.click(80, 421) # 강의 선택2.

    fifth_class = takeaclass(620, 142, 50)
    sixth_class = takeaclass(620, 238, 50)
    seventh_class = takeaclass(620, 334, 30)

    if seventh_class :
        exit(0)

    elif time.strftime("%H:%M") == "05:00" :
        exit(0)