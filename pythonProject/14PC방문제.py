# person = int(input())
# num = list(map(int, input().split()))
# pc = [0] * 100  # 0값으로 초기화된 100개의 리스트 생성
# cnt = 0
# for e in num:
#     if pc[e - 1] != 0: cnt += 1
#     else : pc[e-1] = 1
# print(cnt)

#저항 값 구하기
color = "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
f_name = color.index(input())
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name)) # ** 제곱이란 소리