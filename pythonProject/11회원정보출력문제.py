# 회원정보를 입력 받아서 출력 하는 예제 진행
#
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.

name = str(input("이름 입력 : "))
while True:
    age = int(input("나이를 입력 : "))
    if 0 < age < 200:
        break
    else:
        print("재입력")
while True:
    gender = str(input("성별을 입력 : "))
    if gender == 'm' or gender == 'M':
        gender = "남성"
        break
    elif gender == 'f' or gender == 'F':
        gender = "여성"
        break
    else:
        print("재입력")

while True:
    job = int(input("직업 입력 [1]학생 [2]회사원 [3]주부 [4]무직 : "))
    if job == 1:
        job = "학생"
        break
    elif job == 2:
        job = "회사원"
        break
    elif job == 3:
        job = "주부"
        break
    elif job == 4:
        job = "무직"
        break
    else:
        print("재입력")

print(f"\n이름:{name} \n성별:{gender} \n나이:{age} \n직업:{job}")
