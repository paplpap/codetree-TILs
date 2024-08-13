n = int(input())

arr = []
for i in range(n):
    a = list(input().split())

    if a[0] == 'push_back':
        arr.append(a[1])
    elif a[0] == 'pop_back':
        del arr[-1]
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'get':
        print(arr[int(a[1])-1])