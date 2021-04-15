""" 구구단 출력 """
for i in range(2, 10, 1):  # 구구단의 단수, 가로로 출력
    for j in range(1, 10, 1):
        # print(i * j, end="\t")
        print("%d * %d = %2d" % (i, j, i * j), end="\t")
    print()
print()

for j in range(1, 10, 1):  # 세로로 출력
    for i in range(2, 10, 1):
        print("%d * %d = %2d" % (i, j, i * j), end="\t")
    print()
