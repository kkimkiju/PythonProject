#조건문과 반복문은 제어문이라하고, 이는 수차적인 흐름을 제어하는 목적으로 사용
#파이썬의 조건문 자바의 if문과 switch 문을 결합한 형태와 유사하며, 파이썬은 switch문 없음

# num = int(input("정수를 입력하세요 : "))
#
# if num > 100 :
#     print("입력 값이 100보다 커요.")
# elif num <100 :
#     print("입력 값이 100보다 작아요.")
# else:
#     print("입력 값이 100과 같아요.")

# season = input("지금 계절은 ? ")
# if season == "spring" :
#     print("꽃보러.")
# elif season == "summer" :
#     print("개덥네요")
# elif season == "fall" or season == "autumn" :
#     print("외롭군요")
# elif season == "winter" :
#     print("개춥네요")
# else:
#     print("뭐요")

#성적에 대한 학점 출력하기
#국어,영어,수학 성적을 입력 받아 평균을 구해 등급 출력하기
#평균이 90이상 A, 80이상 B ,70이상 C ,60이상 D ,나머지 F
score = list(map(int, input("국어 영어 수학 성적 입력 ; ").split()))
avg = sum(score)/len(score)
grade = ""
if avg >= 90 : grade = "A"
elif avg >= 80 : grade = "B"
elif avg >= 70 : grade = "C"
elif avg >= 60 : grade = "D"
else: grade = "F"
print(f" 당신의 등급은 {grade} 입니다 ")