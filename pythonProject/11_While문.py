# While문 : 참인 동안 반복 수행, 반복 횟수를 알 수 없을 때 주로 사용
# 입력 받은 정수의 합 구하기
# n = int(input("정수 입력 : "))
# sum = 0
# while n:
#     sum += n
#     n -= 1 # n-- 파이썬에선 안됨
# print(sum)

while True:
    age = int(input("나이를 적으시오 : "))
    if 0 <= age < 200:
        print(f"귀하의 나이는 {age}살 입니다")
        break
    else : print("나이 입력 범위를 벗어났습니다.")

