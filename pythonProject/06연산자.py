# 연산자? 프로그램에서 계산을 위해 사용(사칙,대입,비교,관계,비트 연산 등이 있음)
# 산술연산 : +, -, *, /(나누기), %(나머지), //(몫), **제곱
# 파이썬은 ++, -- 증감 연산자는 없음
i = 10
j = 3
print(i+j)
print(i**j) #10*10*10 제곱 연산
print(f"{i / j:.2f}") # 나누기
print(i//j) # 몫 = 데이터 타입이 없어서 필요함
print(i%j) # 나머지
text = "Python"
print(text * 3)

tax_rate = 0.10
income = int(input("당신의 수입은 얼마입니까? "))
print(f"당신이 내야 할 세금은 {income * tax_rate :.2f} 입니다.")