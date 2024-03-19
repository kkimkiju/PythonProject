# 3개의 정수를 입력받아 최대값/최소값 구하기
from datetime import datetime

# num=list(map(int, input("3개의 정수를 입력하시오 : ").split()))
# print(f"최소값 : {min(num)}")
# print(f"최대값 : {max(num)}")

# 주민번호를 입력받아 생년월일 성별 나이 출력
# from datetime import datetime
# curr_year = datetime.today().year
# jumin = input("주민등록번호 : ")
# year = int(jumin[:2])
# gender = int(jumin[7])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
#
# if gender == 1 or gender == 2:
#     age = curr_year - 1900 - year
# else:
#     age = curr_year - 2000 - year
#
# if gender == 1 or gender == 3:
#     gender_str = "남성"
# else:
#     gender_str = "여성"
#
# print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")

#2개의 문자열을 변수 s와 k에 , 양의 정수를 변수 n에 각각 전달 받아 s문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# s = input("s 문자열 : ")
# k = input("k 문자열 : ")
# n = int(input("정수 입력 : "))
# # print(s[-n:] + k)
# print(s[len(s)-n:] + k)

#여러개의 정수를 입력 받아 합계와 평균 구하기
num2= list(map(int, input("정수 여러개 : ").split(" ")))
print(f"합계 : {sum(num2)}")
print(f"평균 : {sum(num2)/len(num2)}")


