max, min, target = map(int, input().split())
a, b = 0, 0

while(True): 
    while(True):
        # for i in range (2, target, max+1):
        #     if (i<=b):
        #         continue # i를 출력하지 않고 넘어감 # i-=i로 하면 i의 자리가 0으로 출력
        #     print(i, end=' ')
        
        print("\n A 입력: ", end='')
        a_tmp = int(input()) # a_tmp에 임시값을 넣고 조건 충족되면 a로 대입
        if a_tmp>=b+min and a_tmp <= b+max and a_tmp<=target-1:
            a = a_tmp
            print(a)
            break
        else:
            print("잘못입력했습니다.")
    if a == target-1:
        print("A 승리")
        break 

    
    while(True):
        print("B 입력: ", end='')
        b_tmp = int(input())
        if b_tmp>=a+min and b_tmp <= a+max and b_tmp<=target-1:
            b=b_tmp
            print(b)
            break   
        else:
            print("잘못입력했습니다.")

    if  b == target-1:
        print("-1")
        print("B 승리")
        break