n = int(input())
a = input().split()
s = 0

for i in range(n):
    a[i] = int(a[i])

y = min(a) #min(list)하면 리스트중 원소의 최소값 출력 max는 반대
print(y)
