n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n-1, -1, -1): #range(시작, 끝, 증감) 시작 수는 포함, 끝 수는 포함하지 않음
    print(a[i], end=' ')
