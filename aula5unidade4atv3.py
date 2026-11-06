import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dados de treino
x_train = [[1/1], [1/2], [1/3], [1/4], [1/5], [1/6], [1/7]]
y_train = [[2000], [1500], [5000], [4000], [7000], [8000], [6000]]

# Modelo
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Treinamento
model.fit(x_train, y_train, epochs=1000, verbose=0)

# Predição
x_new = tf.constant([[1/8]])
prediction = model.predict(x_new)

print('Predição:', prediction[0][0])

# Visualização
plt.scatter([1/i for i in range(1, 8)], [y[0] for y in y_train], color='blue', label='Treino')
plt.scatter([1/8], prediction[0][0], color='red', label='Predição')
plt.ylabel('Vendas')
plt.xlabel('Mês')
plt.title('Acessório')
plt.legend()
plt.show()
