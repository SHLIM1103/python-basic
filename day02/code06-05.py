# python 은 do-while loop 이 없는 대신, while 무한루프 패턴으로 이용한다

# 전형적인 while loop
# a = input("계속 할까요? (y/n): ")
# while a == "y":
#     a = input("계속 할까요? (y/n): ")

# 무한루프로 do-while loop 를 대신함
while True:
    a = input("계속 할까요? (y/n): ")
    if a == "n":
        break  # 가장 인접한 루프 하나만 탈출하여 아래로 진행
