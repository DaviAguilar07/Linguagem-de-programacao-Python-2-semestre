def square(x):
    """
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x


import doctest

doctest.testmod() # O doctest analisa o >>> e seu resultado esperdo
                  # Caso esteja certo nada acontecerá, caso esteja errado ele avisará onde está o erro.
