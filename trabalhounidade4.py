# Importar bibliotecas necessárias
import tensorflow as tf              # TensorFlow: usado para construir e treinar redes neurais
import pandas as pd                  # Pandas: manipulação de dados em tabelas (não é essencial aqui, mas útil)
from sklearn.datasets import load_iris   # Função para carregar o dataset Iris diretamente do scikit-learn
from sklearn.model_selection import train_test_split   # Para dividir os dados em treino e teste
from sklearn.preprocessing import StandardScaler       # Para normalizar os dados (média 0, variância 1)

# Carregar conjunto de dados Iris
iris = load_iris()                   # Carrega o dataset Iris (150 amostras, 4 características, 3 classes)
X = iris.data                        # Matriz de características (comprimento/largura de sépalas e pétalas)
y = iris.target                      # Vetor de rótulos (0 = setosa, 1 = versicolor, 2 = virginica)

# Pré-processamento dos dados
# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados para melhorar o desempenho do modelo
scaler = StandardScaler()            # Cria o objeto de normalização
X_train = scaler.fit_transform(X_train)   # Ajusta o scaler aos dados de treino e transforma
X_test = scaler.transform(X_test)         # Usa o mesmo scaler para transformar os dados de teste

# Construir o Modelo
# Usamos uma rede neural sequencial (camadas empilhadas)
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),  # Primeira camada oculta com 10 neurônios
    tf.keras.layers.Dense(8, activation='relu'),                     # Segunda camada oculta com 8 neurônios
    tf.keras.layers.Dense(3, activation='softmax')                   # Camada de saída com 3 neurônios (3 classes)
])

# Compilar o modelo
# - Otimizador: Adam (ajusta os pesos automaticamente)
# - Função de perda: sparse_categorical_crossentropy (ideal para classificação multiclasse com rótulos inteiros)
# - Métrica: acurácia (percentual de acertos)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o Modelo
# - epochs: número de vezes que o modelo verá todo o conjunto de treino
# - validation_split: separa 20% dos dados de treino para validação durante o treinamento
# - verbose=0: não mostra o progresso do treinamento
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2, verbose=0)

# Avaliar o Modelo
# Avalia o desempenho no conjunto de teste (dados nunca vistos pelo modelo durante o treino)
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Precisão no conjunto de teste: {accuracy:.2f}")   # Exibe a precisão final

# Fazer Previsões
# O modelo gera probabilidades para cada classe
predictions = model.predict(X_test)          # Matriz de probabilidades (cada linha = uma amostra)
predicted_classes = predictions.argmax(axis=1)  # Pega a classe com maior probabilidade para cada amostra

# Comparar previsões com os rótulos reais
print("\nEspécies previstas:")
for classe in predicted_classes[:10]:
    print(iris.target_names[classe])

print("\nEspécies reais:")
for classe in y_test[:10]:
    print(iris.target_names[classe])
