
a, b = map(int, input().split())
print((bool(a) and bool(not b)) or (bool(not a) and bool(b)))

"""
a, b = map(int, input().split())
if bool(a) ^ bool(b):   # ^는 xor연산자임
    print(True)

else:
    print(False)
"""
