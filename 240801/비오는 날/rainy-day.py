class local:
    def __init__(self, date, number, wh):
        self.date = date
        self.number = number
        self.wh = wh


arr = []
date_list = []


n = int(input())
for i in range(n):
    a = list(input().split())
    if a[-1] == 'Rain':
        arr.append(local(*a))
        date_list.append(a[0])

faster_date_list = sorted(date_list)

for k in range(n):
    if faster_date_list[0] == arr[k].date:
        print(arr[k].date, arr[k].number, arr[k].wh)
        break