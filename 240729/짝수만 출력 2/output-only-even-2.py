b,a = map(int,input().split())
cnt = 0

while cnt < b-a+1:
    if cnt % 2 == 0:
        print(b-cnt, end = ' ') 
    cnt += 1