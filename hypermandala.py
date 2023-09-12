import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hyp2f1
import os

# Genera datos de entrada aleatorios
a_values = np.random.uniform(0.5, 2.5, 100)
b_values = np.random.uniform(1.5, 3.5, 100)
z_values = np.linspace(0, 2, 100)

# Define la red generadora
generator = keras.Sequential([
    # Capas de la red generadora aquí
])

# Compila el modelo
generator.compile(loss='mean_squared_error', optimizer='adam')

# Entrena la red generadora (usando ejemplos reales de funciones hipergeométricas)

# Genera imágenes para diferentes valores de a, b y z
for a, b, z in zip(a_values, b_values, z_values):
    # Genera la imagen usando la red generadora
    generated_image = generator.predict([a, b, z])

    # Mapea la imagen a una escala adecuada para visualizarla
    generated_image = np.interp(generated_image, (generated_image.min(), generated_image.max()), (0, 255))

    # Convierte la imagen a tipo entero
    generated_image = generated_image.astype(np.uint8)

    # Guarda la imagen en un directorio
    directory = 'img'
    os.makedirs(directory, exist_ok=True)
    filename = f'img_a{a}_b{b}_z{z}.png'
    plt.imsave(os.path.join(directory, filename), generated_image, cmap='gray')

# Visualiza o guarda las imágenes generadas
