result = []
while True:
    a = int(input())
    if a >= 30:
        break
    if a < 20:
        break
    result.append(a)
    
aaaa = sum(result)/len(result)

print(f'{aaaa:0.2f}')