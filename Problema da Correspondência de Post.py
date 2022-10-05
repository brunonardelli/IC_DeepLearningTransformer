from itertools import product

pares = (('aa', 'a'), ('ab', 'a'), ('ba', 'a'), ('b', 'bba'))

for tamanho in range(1, 100):
    for i, p in enumerate(product(pares, repeat=tamanho)):
        cima = ''
        baixo = ''
        for peca in pares:
            cima += peca[0]
            baixo += peca[1]
        if cima == baixo:
            print(pares)
            print(cima)
            print(baixo)

