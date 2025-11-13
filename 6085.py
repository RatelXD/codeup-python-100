w, h, b = map(int, input().split())
pixel = w*h*b/8/1024/1024
print('%0.2f' %pixel ,"MB")

#round() 함수를 사용하면 소수점을 정해진 대로 전부 표시하지 않는다. (0으로 생략가능한 경우 생략함)
