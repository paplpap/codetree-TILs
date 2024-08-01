class market:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

        print(f'product {code} is {name}')


m1 = market()
m2 = market(*tuple(input().split()))