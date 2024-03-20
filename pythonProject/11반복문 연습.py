# 사각형 찍기 : 정수값을  n을 입력 받아 n*n크기의 행렬을 출력하는 프로그램 작성
# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:3}", end="")
#     if i % n == 0: print()  # 입력 받은 수의 배수마다 줄 바꿈

# 별 찍기 1번
# n = int(input())
#  for i in range(n): #초기값 0 , 최종값은 입력값 미만, 증가값 1
#      for j in range(i+1):
#          print("*", end="")
#      print()
#
#  별 찍기 2번
#  for i in range(n):
#      for j in range(n-i):
#          print("*", end="")
#      print()
#
# 별 찍기 3번
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n - i):
#         print("*", end="")
#     print()

# for문에서 continue 사용
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i, end=" ")

# for문을 반대로 반복하기
# for i in range(10, 0 - 1, -1): # 10에서부터 1씩 감소 시키면서 0까지 출력
#      print(f"index : {i}")

# for문으로 알파벳 출력하기 :
# chr(유티코드값을 입력 받아 문자 출력)
# ord(문자의 유니 코드 값을 반환)

for i in range(ord("A"), ord("Z") + 1):  # A~Z까지
    print(chr(i), end="")
print()

for i in range(65, 91):
    print(chr(i), end=" ")
print()
