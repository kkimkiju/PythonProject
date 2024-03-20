# 사용자의 입력을 처리하는 input() 함수, 기본값은 문자열로 입력됨
# name = input("이름을 입력 하세요 : ")
# print(name)
# kor = int(input("국어 성적을 입력하세요 : "))
# print(f"국어 : {kor}


# map은 2개의 인자값인데 첫 번째 - 콜백 함수자리, 두 번째 - 입력되는 데이터
# map의 특성은 입력 받은 데이터를 동일한 개수 만큼 변환해서 반환
# kor,eng,mat = map(int,input("국어 영어 수학 : ").split())
# print(f"국어 : {kor}, 영어 : {eng}, 수학 : {mat}")

# name,addr = input("이름과 주소 입력 : ").split() #split의 기본값은 공백
# print(f"이름 : {name}, 주소 : {addr}")

# 입력 제한 없이 다 받고 싶은 경우
# score = list(map(int, input("성적을 마음대로 입력 : ").split()))
# print(f"성적을 리스트 출력 : {score}")

# #split 활용
# hour, min, sec = input("시:분:초 : ").split(":")
# print(f"{hour}시 {min}분 {sec}초")

hour, min, sec, = map(int,input("시:분:초 ").split(":"))
if(hour > 12):
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}초") # 02 = 두 자리 차지
else:
    print(f"오전{hour:02}시{min:02}분{sec:02}초")