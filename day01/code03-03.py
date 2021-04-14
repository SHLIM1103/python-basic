b = True
print(b)
print(type(b))
print(type(1))
print(type("1"))

i = 0
f = 0.
s = "0"
print(type(i))
print(type(f))
print(type(s))

b = True
i = 0
f = 0.
s = ''  # python 은 "" 와 ''가 같다, 다만 시작과 끝은 모두 동일하게 맞춰야 한다
print(type(b), type(i), type(f), type(s))

i = 200 + 200
print(i)
j = i + 100
print(j)

i = j = 300  # i 와 j 를 모두 300으로 바꿔라
print(i, j)
i += 100
print(i)
++i ;
print(i)  # python 은 증감연산자가 없다

k = 0
print("k =", k)  # 변수선언은 반드시 해야 한다

myVar = 100
print(type(myVar))
myVar += 0.1
print(type(myVar))  # python 은 자동으로 형변환을 한다
