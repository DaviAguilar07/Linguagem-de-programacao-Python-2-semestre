import unittest
import doctest

def lista(lista1): # Esse método realiza a soma do listao
    #  print(sum(lista1))
     return sum(lista1)

listao = [10, 20, 30, 40]
lista(listao) # Passando o valor para o método.


lista_negativo = []
for colocacao, i in enumerate(listao):
     if i < 0:
        lista_negativo.append(i)


# ==========ASSERT========== Testando se a lista está vazia ou preenchida

def assert1(listao, lista_negativo):
     assert listao != [] # A lista está vazia.
     assert lista_negativo == [] # Existe número negativo na lista.
     return 'A lista está preenchida e com apenas números positivos.'
print(assert1(listao, lista_negativo))


# ==========DOCTEST========== Testando se as posições estão corretas dentro da lista

def posicao(listao, i):
    """
    >>> posicao([10, 20, 30, 40], 0)
    10
    >>> posicao([10, 20, 30, 40], 1)
    20
    >>> posicao([10, 20, 30, 40], 2)
    30
    >>> posicao([10, 20, 30, 40], 3)
    40
    """
    return listao[i]
doctest.testmod()


# ==========UNITTEST========== Testando se a soma dos valores da lista está correto
class teste(unittest.TestCase):
     def test_lista_valor(self):
          self.assertEqual(lista(listao), 100)

if __name__ == '__main__':
     unittest.main()
     print()
