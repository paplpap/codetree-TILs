n = int(input()) 

arr = []
for _ in range(n):
    arr.append(int(input()))


result = []


for i in range(n): # 시작점
    cnt = 0
    for j in range(n): #가중치
        
        cnt += arr[i]*j
        i += 1
        if i >= n:
            i -= n
        
    result.append(cnt)
        

print(min(result))