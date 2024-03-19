hour, min = map(int, input("시간 입력 : ").split(":"))
tmp = (hour * 60) + min
if tmp < 45:
    tmp = (24 * 60) + min
tmp -= 45

print(f"{tmp // 60} {tmp % 60}")




3시 20분

155 //60 2 35

00 20

1415 23

23시 35분