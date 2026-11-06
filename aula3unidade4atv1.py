def valor(x, y):
    assert y != 0 # O assert não deixa executar o programa, pois a condição será falsa.
    return x / y # O assert retornará um erro.

result = valor(6,0)
print(result) # Divisão por zero.
