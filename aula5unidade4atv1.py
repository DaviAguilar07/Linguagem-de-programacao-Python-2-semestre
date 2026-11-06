def calcularcomissao(venda, percentual):
    return (venda * percentual / 100)

def assert1(percentual):
    assert percentual <= 20 # Comissão acima do permitido
    return f'Comissão permitida.'

print('=====Cálculo de comissão para o vendedor=====')
venda = float(input('Qual o valor do produto vendido? '))
percentual = float(input('Qual o valor da comissão do vendedor em %? '))

comissao = calcularcomissao(venda, percentual)

assert1(percentual)

print(f'O vendedor tem {percentual}% de comissão. Portanto ele receberá R${comissao} da venda.')
