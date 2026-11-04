texto = 'O Python é a linguagem de programação do momento.'

tamanho = len(texto)
alvo = 'Python' in texto
quantidade = texto.count('e')
# letras = texto[:5]

print(f"O tamanho do texto é {tamanho}")
print(f"Existe a palavra 'Python' no texto? {alvo}")
print(f"Quantos 'e' tem no texto? {quantidade}")
print(f"As cinco primeiras letras do texto são: {texto[:5]}")
