m1, d1, m2, d2 = map(int,input().split())
A = input()

data = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data_cnt = 0
result = 0

while True:

    if m1 in [1,3,5,7,8,10,12]:
        if d1 > 31:
            d1 = 1
            m1 += 1
    
    if m1 in [4,6,9,11]:
        if d1 > 30:
            d1 = 1
            m1 += 1

    if m1 == 2:
        if d1 > 29:
            d1 = 1
            m1 += 1
    
    
    if A == data[data_cnt]:
        result += 1
    #print('m1:',m1,'d1:',d1)

    data_cnt += 1
    
    if data_cnt == 7:
        data_cnt = 0


    if (m1 == m2) and (d1 == d2):
        break
    

    d1 += 1


print(result)