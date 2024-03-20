# for문은 정해진 범위 만큼 반복할 때 주로 사용
# for 요소 int 시퀀스: 시퀀스는 리스트, 튜플, 문자열 등을 의미, 자바의 향상된 for와 유사
fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
for e in fruits:
    print(e, end="-")
print()

# for 변수 in range(시작값, 종료값, 증감값): 자바의 일반적인 for문과 유사
# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n+1): #1부터 n까지 순회 (종료값은 미만 개념), 증감값은 생략하면 1씩 증가
#     sum += i
# print(sum)

# 이중 for문 사용하기
# n = int(input("정수를 입력 : "))
# for i in range(0,n):
#     for j in range(0,n):
#         print("*", end= " ")
#     print()

# 구구단

# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")
#     print("===================")

# 이중 for문과 조건문 사용
# n = int(input("정수를 입력 하세요 :"))
# for i in range(0,n):
#     for j in range(0,n):
#         if j % 2 ==0:
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

n = int(input())
for i in range(n):  # 0부터 n-1 까지
    for j in range(n - i):
        print("*", end="")
    print()

n = int(input("정수를 입력하세요: "))
for i in range(n):
    print(' ' * i + '*' * (n - i))

n = int(input())
for i in range(n):
    for k in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print()