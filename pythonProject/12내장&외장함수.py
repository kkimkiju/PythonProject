# 내장함수? 별도의 import 없이 사용할 수 있도록 내장된 함수를 말함
print(max(32, 45, 48, 57, 23))
print(min(32, 45, 48, 57, 23))

# sum에는 리스트 혹은 튜플 형태로 전달
print(sum((26, 34, 45, 67, 45)))
print(sum([26, 34, 45, 67, 45]))

value = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  # 튜플
print(sum(value))
print(f"평균 {sum(value) / len(value)}")

# divmod() = 몫과 나머지
print(divmod(sum(value), 4))  # sum을 4로 나눈 몫 13 나머지 3

# 외장 함수 : 파이썬의 표준 모듈이지만 import해야 사용 가능
import random

for i in range(10):
    # rand = random.randint(0, 4)  # 0~4사이의 임의의 정수 반환(4 포함)
    # rand = random.randrange(0, 4)  # 0~4미만
    rand = random.randrange(4)  # 0~4미만
    print(rand, end=" ")

# 날짜 및 시간 관련 처리 모듈
from datetime import datetime  # datetime 모듈에서 datetime 함수만 import

datetime.today()  # 현재 날짜 가져오기
print(datetime.today().year)  # 현재 연도 가져오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 달력 생성
import calendar

print(calendar.calendar(2024, m=5))
print(calendar.month(2024, 3))

# mate 모듈
import math

print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.ceil(1.0000000000001))
print(math.floor(1.0000000000001))


