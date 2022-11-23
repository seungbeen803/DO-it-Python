# 외장함수
import sys
print(sys.argv)

import time
for i in range(5):
    print(i)
    time.sleep(1) # 1초 텀을 두고 실행
print(time.time()) # 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간 초

# random
import random
lotto = sorted(random.sample(range(1, 46), 6))
print(lotto)

import webbrowser
webbrowser.open("http://googl.com")
# webbrowser.open_new("http://google.com")