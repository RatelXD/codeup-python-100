max, min, target = map(int, input().split())
a, b = 0, 0

while(True): 
    while(True): 
        
        print("A 입력: ", end='')
        a = int(input()) # a_tmp에 임시값을 넣고 조건 충족되면 a로 대입
        if a>=b+min and a <= b+max and a<=target-1:
            break
        else:
            print("잘못입력했습니다.")
    for j in range(2, target, max-1):
        if a == j:
            for i in range (2, target, max+1):
                if (i<=b):
                    continue # i를 출력하지 않고 넘어감 # i-=i로 하면 i의 자리가 0으로 출력
                print(i, end=' ')
            break 
        else:
            print("-1")
            break


    
    