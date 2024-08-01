class local:
    def __init__(self, name, number, home):
        self.name = name
        self.number = number
        self.home = home


arr = []

n = int(input())
for i in range(n):
    arr.append(local(*list(input().split())))

name_arr = []

for i in range(n):
    name_arr.append(arr[i].name)

name_arr.sort()
name = name_arr[-1]
aaa = arr[name_arr.index(name)]

print('name',aaa.name)
print('addr',aaa.number)
print('city',aaa.home)