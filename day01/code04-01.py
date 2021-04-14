a = 100
print(a + 1)
print(str(a) + "1")  # str() 로 강제 문자변환

a = "100"
print(int(a) + 1)  # int() 로 강제 정수변환

a = "12.3"
print(float(a)+ 0.1)  # float() 로 강제 실수변환

a = 100
b = 100
print(a == b)

print(True and True)
print(True and False)
print(True or False)
print(not True)

print(ord('A'))  # 유니코드에서 ordinal(순서)값이 출력
print(ord('가'))

print(chr(66))  # 유니코드 숫자를 문자로 변경한 값이 출력
print(chr(44033))
