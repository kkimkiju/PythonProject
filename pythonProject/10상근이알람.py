hour, min = map(int, input("시간 입력 : ").split(":"))
tmp = (hour * 60) + min
if tmp < 45:
    tmp = (24 * 60) + min
tmp -= 45

print(f"{tmp // 60}:{tmp % 60}")
