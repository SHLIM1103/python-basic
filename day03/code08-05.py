s = "파이썬"
print(s.center(10))  # 결과:    파이썬     -> 총 n 길이 중 가운데 정렬해 삽입
print(len(s.center(10)))  # 결과: 10

print(s.center(10, "*"))  # 결과: ***파이썬**** -> 총 n 길이를 특정 문자로 채운 후 가운데 정렬
print(s.ljust(10, "*"))  # 결과: 파이썬******* -> 총 n 길이를 특정 문자로 채운 후 좌측정렬
print(s.rjust(10, "*"))  # 결과: *******파이썬 -> 총 n 길이를 특정 문자로 채운 후 우측정렬

print(s.zfill(10))  # 결과: 0000000파이썬 -> 총 n 길이를 0으로 채운 후 우측정렬(cf. 숫자는 %05d)

print("1234".isdigit())  # 결과: True -> 해당 문자열이 모두 숫자인지 여부를 T/F로 출력
print("a234".isdigit())  # 결과: False -> 한 글자라도 숫자가 아닌 문자가 포함되어 있으면 False

print("abcd".isalpha())  # 결과: True -> 해당 문자열이 모두 문자인지 여부를 T/F로 출력
print("a12bcd".isalpha())  # 결과: False

print("a12bcd".isalnum())  # 결과: True -> 해당 문자열이 모두 문자 또는 숫자인지 여부를 T/F로 출력
print("a1!bcd".isalnum())  # 결과: False -> 해당 문자열에 특수기호가 포함되어 있으면 False

print("a1bcd".islower())  # 결과: True -> 해당 문자열 중 문자가 모두 소문자로 구성되어 있는지 여부를 T/F로 출력
print("A1bcd".islower())  # 결과: False
print("A1BCD".isupper())  # 결과: True -> 해당 문자열 중 문자가 모두 대문자로 구성되어 있느닞 여부를 R/F로 출력
print("a1BCD".isupper())  # 결과: False

print("A BC".isspace())  # 결과: False -> 해당 문자열이 모두 공백인지 여부를 T/F로 출력
print("  ".isspace())  # 결과: True
