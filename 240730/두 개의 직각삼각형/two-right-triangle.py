n= int(input())


ae = '*'
for i in range(n,0,-1):
    print(ae*i,end = '')

    print(' '*2*(n-i),end='')

    print(ae*i)