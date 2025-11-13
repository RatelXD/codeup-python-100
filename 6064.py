a, b, c = map(int, input().split())
print(a) if a<b and a<c else (print(b) if b<c else print(c))

"""
a, b, c = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)

d = a if a<b else b
e = d if d<c else c

print(e)
"""
