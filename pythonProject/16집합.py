# 집합 자료형은 주로 중복 제거용 사용
# 순서를 보장하지 않음
# 중복 불가
# mutable(Read/Write 가능)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
# 합집합
s3 = s1.union(s2)
s3 = s1 | s2
# 교집합
s3 = s1.intersection(s2)
s3 = s1 & s2
# 차집합
s3 = s1.difference(s2)
s3 = s1 - s2
print(s3)

#중복제거 로또 쉬운 방법
import random
lotto = set()
while True:
    num = random.randrange(1,46)
    lotto.add(num)
    if len(lotto) == 6 : break
print(lotto)