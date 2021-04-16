s = "  파 이 선  "
print(len(s))  # 결과: 9 -> 공백도 한글자로 처리
print(s.strip())  # 결과: 파 이 선 -> 좌우 공백 제거
print(len(s.strip()))  # 결과: 5
print(s)  # 결과: s -> 문자열은 변경되지 않았다

print(s.lstrip())  # 결과: 파 이 선   -> 왼쪽 공백 제거
print(len(s.lstrip()))  # 결과: 7
print(s.rstrip())  # 결과:   파 이 선 -> 오른쪽 공백 제거
print(len(s.rstrip()))  # 결과: 7

print(s.replace(" ", ""))  # 결과: 파이선 -> a 를 b 로 교체
print(len(s.replace(" ", "")))  # 결과: 3
