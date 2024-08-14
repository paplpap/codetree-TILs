n = int(input())

arr = []
dp = []

for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

    dp.append([0]*n)


def init():
    
    for i in range(n):
        
        dp[0][i] += arr[0][i]

    
    for i in range(1,n):
    
        dp[i][0] += arr[i][0]

init()


for i in range(1,n):
    for j in range(1,n):
        # a = min(dp[i-1][j],dp[i][j-1])
        # if a < arr[i][j]:
        #     dp[i][j] = a
        # else:
        #     dp[i][j] = arr[i][j] 
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), arr[i][j])

print(dp[n-1][n-1])