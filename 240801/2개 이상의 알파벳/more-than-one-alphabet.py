A = input()

def aa(A):
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            print('Yes')
            exit(0)
    print('No')

    

aa(A)