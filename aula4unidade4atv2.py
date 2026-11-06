import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model


# Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

# Modelo Autoencoder Simples

input_layer = Input(shape=(2,))

encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2)(encoded)


autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

# Previsão

prediction_unsupervised = autoencoder.predict(X_unsupervised)
print('Predição Não Supervisionada:', prediction_unsupervised)
