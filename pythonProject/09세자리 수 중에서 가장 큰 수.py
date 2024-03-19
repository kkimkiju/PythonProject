num = int(input("세 자리 정수를 입력하세요"))

num1 = num // 100  # 몫을 구해야 해서 //로 함
num2 = (num % 100) // 10
num3 = num % 10

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else: print(num3)

alba = int(input("근무를 고르시오 [1]주간 [2]야간"))
time = int(input("근무 시간을 입력해 주세요 : "))
time_pay = 9620
money = 0

if alba == 1:
    zuya = "주간"
    money = time * time_pay

else:
    zuya = "야간"
    money = time * (time_pay * 1.5)

print(f"당신의 {zuya}근무 급여는 {money}원 입니다.")
