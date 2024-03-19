# 파이썬은 변수 선언시 데이터 타입을 지정하지 않으며, 변수의 값이 대입될 때 형이 결정됨.
# number = 200
# number2 = 3.14
# strs = ""
# bools = True
# print(type(number)) #type() : 변수의 데이터형을 확인
# print(type(str))
# print(type(bool))
# print(type(number2))

# 형변환 : 선언된 변수에 값이 할당되는 순간 형이 결정, 이후 다른 데이터형으로 변경할 때 사용
print(10 + int("10"))
print("나이 : " +str(30))
print(0.1 * float("512.34"))

var = "" # 공백은 거짓
number = -12321 # 0,None은 거짓
print(bool(number)) # boolean 값의 거짓 : ""(공백), 0, False, None