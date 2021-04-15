""" 이등변삼각형 만들기 """
for i in range(1, 6, 1):  # 행
    for j in range(1, 6 - i, 1):  # 빈칸
        print(" ", end="")
    for k in range(1, 2 * i, 1):  # 별
        print("*", end="")
    print()
