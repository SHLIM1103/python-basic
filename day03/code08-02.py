s = "aBcD"
print(s.upper())  # 결과: ABCD -> 모두 대문자로
print(s.lower())  # 결과: abcd -> 모두 소문자로
print(s.swapcase())  # 결과: AbCd -> 대-소문자 교체
print(s.title())  # 결과: Abcd -> 첫글자만 대문자
print()

s = "abcdabcd"
print(s.count("bc"))  # 결과: 2 -> 해당 문자열의 개수
print(s.find("bc"))  # 결과: 1 -> 해당 문자열을 좌측부터 찾았을 때 첫 인덱스 번호
print(s.rfind("bc"))  # 결과: 5 -> 해당 문자열을 우측부터 찾았을 때 첫 인덱스 번호
print(s.find("bc", 3))  # 결과: 5 -> index 3 이후부터 해당 문자열을 찾았을때 인덱스 번호
print(s.find("e"))  # 결과: -1 ->  해당 문자열 검색 실패시 -1 이 출력
print()

print(s.startswith("ab"))  # 결과: True -> 해당 문자열로 시작하는지 여부
print(s.startswith("bc"))  # 결과: False
print(s.endswith("cd"))  # 결과: True -> 해당 문자열로 끝나는지 여부
print(s.endswith("de"))  # 결과: False

print(s.startswith("bc", 1))  # 결과: True -> index 1 이후부터 해당 문자열로 시작하는지 여부
print(len(s))  # len은 메소드가 아닌 function !
