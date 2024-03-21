# 계좌 개설
def open_account(name):  # 매개변수와 반환값이 있는 함수 선언
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name


def deposit(balance, input):  # 잔액과 입금액을 매개변수로 전달 받음 (입금)
    print(f"{input}원이 입금 되었습니다. 잔액은 {balance + input}원 입니다.")
    return balance + input


def withdraw(balance, input):
    if balance >= input:
        print(f"{input}원이 출금 되었습니다. 잔액은 {balance - input}원 입니다.")
        return balance - input
    else:
        print(f"잔액이 부족합니다.")
        return balance


balance = 0  # 현재잔액
name = open_account("김기주")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}님의 잔액은 {balance}원 입니다")
