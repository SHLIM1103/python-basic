print(2 ** 3)
print(pow(2, 3))
print(100 ** 100)
print(9 / 2)
print(9 // 2)  # 결과값에서 나머지를 제외한 몫만 구하기
print(9 % 2)   # 결과값에서 몫을 제외한 나머지만 구하기
print(3.14E5)
print(0xFF, 0o77, 0b1111)           # 16진수, 8진수, 2진수를 10진수로 변환
print(hex(255), oct(63), bin(15))   # 10진수를 16진수, 8진수, 2진수로 변환
print()

a = (100 == 100)
print(a)

b = "파이선\n만세"
print(b)
b = """파이선
만세"""
print(b)  # """는 화면에 보이는 그대로 출력 (cf. '''는 주석)
b = "파이선\
만세"
print(b)
