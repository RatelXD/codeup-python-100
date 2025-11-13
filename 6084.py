h, b, c, s = map(int, input().split())
sum = (h*b*c*s)/8/1024/1024
print('%0.1f'%sum, "MB")
# print(round(h*b*c*s/8/1024/1024, 1), "MB")
# round(수식, 소수점 몇 번째 자리까지 반올림해서 출력할건지)
"""
h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1), "MB")
"""
