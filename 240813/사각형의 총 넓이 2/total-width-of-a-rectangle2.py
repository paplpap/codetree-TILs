n = int(input())
arr = [[0]*201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(100+x1,100+x2):
        for j in range(100+y1,100+y2):
            arr[i][j] = 1


cnt = 0
for p in arr:
    for j in p:
        if j == 1:
            cnt += 1

print(cnt)
    


# x1, x2, y1, y2 = 2,4,5,8

# arr = [ [0]*9 for _ in range(5) ]

# for i in range(x1,x2):
#     for j in range(y1,y2):
#         arr[i][j] = 1


# for p in arr:
#     print(p)