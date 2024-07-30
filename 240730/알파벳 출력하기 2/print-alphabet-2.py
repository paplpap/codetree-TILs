n = int(input())

al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

cnt = 0
for i in range(n):
    print(i*'  ',end = '')
    for j in range(n-i,0,-1):
        if cnt == 26:
            cnt = 0
        print(al[cnt], end = ' ')
        cnt += 1
        
    print()