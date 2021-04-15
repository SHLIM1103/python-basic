""" 누적합이 100 을 넘는 순간의 카운터와 합 출력 """
hap = 0

for i in range(1, 11, 1):
    hap += i
    if hap > 10:
        break
print(i, hap)

i = 0
while hap <= 10:
    i += 1
    hap += i
print(i, hap)

i = 1
while True:
    hap += i
    i += 1
    if hap > 100:
        break
print(i, hap)
