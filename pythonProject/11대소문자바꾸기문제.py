# 문자열을 입력 받아 대문자는 소문자로, 소문자는 대문자로 변경하기
# rst = ""
# for e in input("단어 입력 : "):
#     if e.islower():
#         rst += e.upper()
#     else:
#         rst += e.lower()
# print(rst)


print("정수 입력")
a = int(input())
b = int(input())
c = int(input())

sum = str(a*b*c)
for i in range(10) : #10번째 숫자까지 찾음
    print(sum.count(str(i))) #i가 0의자리부터 9의 자리까지 포함된 숫자 표출