# 리스트란? 연속적으로 저장되는 형태의 자료형
# 크기가 동적으로 변함
# 자바와 다른 점은 여러가지 데이터 타입이 섞여 있을 수 있음
# 리스트 내에 리스트가 존재할 수 있음
# 리스트는 읽기/쓰기 가능, 튜플은 동일한 구조이지만 읽기만 가능
# number = [1, 2, 3, 4, 5, 6, 7]
# fruits = ['apple', 'banana', 'orange']
# mixed = [1234, 'apple', True, 3.14, ['EV6', 'Santafe', "Sorento"]]
# print(number[1])
# print(fruits[0])
# print(fruits[1][2])
# print(mixed[4][2])  # mixed 4번(자동차들)에 2번이라는 소리
# print(mixed[4][2][5])  # mixed 4번(자동차들)에 2번(소렌토에) 5번째 글자
# print(mixed[3])
# print(len(mixed[4]))
# print(mixed[4][2][-1])
#
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# list_c = list_a + list_b
# print(list_c)
#
# new_list = [1, 2, 3]
# new_list.append(4)
# new_list.append(5)
# new_list.insert(1, 1000)  # 1번 인덱스에 값추가
# print(new_list)

# 리스트에서 값 제거하기 : pop, remove, clear
# pop : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제
# print(new_list.pop(1))  # pop()< 해당 인덱스의 값을 반환하고 제거 / 빈 칸일 시 마지막 인덱스 삭제
# new_list.remove(3) #해당 값을 제거, 동일한 값이 여러개 존재하는 경우 낮은 인덱스 값 제거
# # new_list.clear() #내용을 전부 제거하지만 리스트는 남아있음
# del new_list[3]
# print(new_list) #해당 인덱스의 값 제거


# 변수와 리스트의 차이 비교
# kor, eng, mat = map(int, input().split())
# total = kor + eng + mat
# print(total/3)

# score = list(map(int, input().split()))
# print(sum(score) / len(score))

# 중복 제거

my_list = ["A", "B", "C", "D", "E", "B", "C"]
new_list = []
for e in my_list:
    if e not in new_list:
        new_list.append(e)
print(new_list)

# 리스트 순회하기
x = ["John", "George", "Paul", "Ringo"]
# for e in x:
#     print(e, end= " ")
for i in range(len(x)):
    print(x[i], end=" ")

# 1~45까지의 로또 번호 6개를 자동 생성하기

import random

ls = []
while True:
    rand = random.randrange(1, 46)
    if rand not in ls:
        ls.append(rand)
    if (len(ls)) == 6:
        break

print(ls)
# ============================================
# print("숫자 입력 : ", end=" ")
# num = list(map(int, input().split()))
#
# jjak = []
# hol = []
#
# for e in num:
#     if e % 2 == 0:
#         jjak.append(e)
#     else:
#         hol.append(e)
#
# print(f"홀수 : {hol}")
# print(f"짝수 : {jjak}")
# =============================================

num = list(map(int, input("정수 입력 : ").split()))
even = list(filter(lambda x:x % 2 == 0, num)) # num에 있는 1을 넣는다 가정하면 첫 번째 x는 넣은 숫자 두 번째 x는 %2 하는 계산식을 의미
odd = list(filter(lambda x:x % 2 == 1, num))
print(f"홀수 {odd}")
print(f"짝수 {even}")