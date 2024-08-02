n = int(input())
arr = list(map(int,input().split()))

new_arr = sorted(arr)


for i in arr:
    cnt = 0
    for j in new_arr:
        cnt += 1 
        if i == j:
            print(cnt, end = ' ')
            new_arr[new_arr.index(j)] = 0
            break