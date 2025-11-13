a = int(input())
print(not bool(a))

"""
a = bool(int(input())) # 이렇게 겹치면 input(), int(), bool() 순서로 한 단계씩 처리됨
print(not a)
"""
