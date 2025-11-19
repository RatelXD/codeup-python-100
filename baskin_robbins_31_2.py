print("규칙 제시 A: ", end ='')
min, max, target = map(int, input().split())
print("B: ", end = '')
if (min < max) and (max * 10 < target) and (min < 10000) and (max < 10001) and (target < 200000): 
    for i in range(((target-min)%(min+max)), (target-min)+1, (min+max)):
        if min <= i <= max:
            a = list(range(((target-min)%(min+max)), (target-min)+1, (min+max)))
            print(*a)
            break 
        else:
            print("-1")
            break
        
# max * 10 < target 게임이 최소 10턴은 진행되어야함
# (target-min)%(min+max)

    
    