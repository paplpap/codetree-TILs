n, m = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

visited = [False for i in range(n+1)]
cnt = 0

def dfs(ver):
    global cnt

    for curr_v in graph[ver]:
        if not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)

for i in range(m):
    v1, v2 = list(map(int,input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(cnt)