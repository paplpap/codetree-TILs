n = int(input())

arr = []
dp = []

for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

    dp.append([0]*n)



def initialize():
    # 시작점의 경우 dp[0][0] = num[0][0]으로 초기값을 설정해줍니다

    dp[0][0] = arr[0][0]
    
    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], arr[i][0])
    
    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], arr[0][j])
        
        
# 초기값 설정
initialize()


for i in range(1,n):
    for j in range(1,n):
        # a = min(dp[i-1][j],dp[i][j-1])
        # if a < arr[i][j]:
        #     dp[i][j] = a
        # else:
        #     dp[i][j] = arr[i][j] 
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), arr[i][j])

print(dp[n-1][n-1])