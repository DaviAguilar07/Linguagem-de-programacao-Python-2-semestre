lista = ['Python', 'Java', 'CSS', 'C++']

print(f"Antes da mudança: {lista}")

# O conteúdo da lista vai mudar.
lista = [item.lower() for item in lista]
print(f"Depois da mudança: {lista}")
