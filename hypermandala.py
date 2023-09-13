import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os

# Genera datos de entrada aleatorios
a_values = np.random.uniform(0.5, 2.5, 100)
b_values = np.random.uniform(1.5, 3.5, 100)
z_values = np.linspace(0, 2, 100)

# Define la red generadora
generator = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(3,)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(784, activation='sigmoid'),  # Capa de salida, con activación 'sigmoid' para valores en [0, 1]
    keras.layers.Reshape((28, 28))  # Ajusta la forma para que sea una imagen de 28x28 píxeles
])

# Compila el modelo
generator.compile(loss='mean_squared_error', optimizer='adam')

# Entrena la red generadora (usando ejemplos reales de funciones hipergeométricas)

# Genera imágenes para diferentes valores de a, b y z
for a, b, z in zip(a_values, b_values, z_values):
    # Genera la imagen usando la red generadora
    generated_image = generator.predict(np.array([[a, b, z]]))  # Se pasa un array 2D con un solo ejemplo

    # Mapea la imagen a una escala adecuada para visualizarla
    generated_image = np.interp(generated_image, (generated_image.min(), generated_image.max()), (0, 255))

    # Convierte la imagen a tipo entero
    generated_image = generated_image.astype(np.uint8)

    # Añade una dimensión para convertir la imagen en escala de grises a RGB
    generated_image_rgb = np.expand_dims(generated_image, axis=-1)

    # Guarda la imagen en un directorio
    directory = './img'
    os.makedirs(directory, exist_ok=True)
    filename = f'img_a{a}_b{b}_z{z}.png'
    plt.imsave(os.path.join(directory, filename), generated_image_rgb, cmap='gray')

# Visualiza o guarda las imágenes generadas
