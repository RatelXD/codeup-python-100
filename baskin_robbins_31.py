a, b = 0, 0
a_list=[2, 6, 10, 14, ]
while(True): 
    while(True):
        for i in range (2, 31, 4):
            if (i<=b):
                continue # i를 출력하지 않고 넘어감 # i-=i로 하면 i의 자리가 0으로 출력
            print(i, end=' ')
        
        print("\nA 입력: ", end='')
        a_tmp = int(input())
        if a_tmp>b and a_tmp <= b+3 and a_tmp<=30:
            a = a_tmp
            print(a)
            if a==30:
                print("A 승리")
            break
        else:
            print("잘못입력했습니다.")
    if a == 30 or b == 30:
        break 

    
    while(True):
        print("B 입력: ", end='')
        b_tmp = int(input())
        if b_tmp>a and b_tmp <= a+3 and b_tmp<=30:
            b=b_tmp
            print(b)
            if b==30:
                print("-1")
                print("B 승리")
            break
        else:
            print("잘못입력했습니다.")

    if a == 30 or b == 30:
        break
        

# a_list안에 2~30까지 4의 배수의 리스트를 만들어서 b보다 큰 원소만 출력되게하는 방법
# 2~30까지 중 b보다 큰 값만 출력되게


# a, b = 0, 0
# while(True): 
#     if a>b and a <= b+3:
#         a = int(input())
#         print(a)
#         if a==30:
#             print("A 승리")
#             break
#     else:
#         print("잘못입력했습니다.")
#     if b>a and b <= a+3:
#         b = int(input())
#         print(b)
#         if b==30:
#             print("B 승리")
#             break
#     else:
#         print("잘못입력했습니다.")
