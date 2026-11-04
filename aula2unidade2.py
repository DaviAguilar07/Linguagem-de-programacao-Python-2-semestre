import math
import numbers as np

participantes = [{'Nome': 'João', 'Localização': 'Brasil', 'Afiliaçao': 'Universidade A', 'Interesses': ['Fisica', 'Astronomia']},
                 {'Nome': 'Ádria', 'Localização': 'EUA', 'Afiliaçao': 'Universidade B', 'Interesses': ['Psicologia', 'Inglês']},
                 {'Nome': 'Luisa', 'Localização': 'Brasil', 'Afiliaçao': 'Universidade C', 'Interesses': ['Biologia', 'Astronomia']}]
# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante['Localização'] for participante in participantes)

# Usando um dicionário para categorizar afiliações
Afiliaçoes = {}
for participante in participantes:
    afiliaçao = participante['Afiliaçao']
    if afiliaçao not in Afiliaçoes:
        Afiliaçoes[afiliaçao] = []
    Afiliaçoes[afiliaçao].append(participante['Nome']) #Atenção

# Usando NumPy para analisar áreas de interesse

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['Interesses']])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

print(f'Regiões dos participantes:', regioes)
print(f'Afiliação dos participantes:')
for afiliaçao, nomes in Afiliaçoes.items():
    print(f'{afiliaçao}: {', '.join(nomes)}')
print(f'Área de interesse mais popular:', area_mais_popular)
