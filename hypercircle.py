import pygame
import numpy as np
import math

# Configuración de Pygame
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mandalas Hipergeométricas")

# Función para generar parámetros válidos y ángulo
def generate_valid_params():
    a = np.random.uniform(0.5, 1.5)
    b = np.random.uniform(1.5, 3.5)
    z = np.random.uniform(0, 2)
    angle = np.random.uniform(0, 2 * np.pi)  # Ángulo aleatorio
    return a, b, z, angle

# Función para aproximar visualmente una función hipergeométrica en un círculo
def draw_hypergeometric_shape(a, b, z, angle, num_points=100):
    points = []
    for i in range(num_points):
        t = i * (2 * np.pi) / num_points
        x = width // 2 + int(100 * (a + z) * math.cos(angle + t))
        y = height // 2 + int(100 * (b + z) * math.sin(angle + t))
        points.append((x, y))
    pygame.draw.polygon(screen, (255, 255, 255), points, 1)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar parámetros aleatorios
    a, b, z, angle = generate_valid_params()

    # Dibujar aproximación visual de una función hipergeométrica
    draw_hypergeometric_shape(a, b, z, angle)

    pygame.display.flip()

pygame.quit()
