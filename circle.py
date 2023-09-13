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

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar parámetros aleatorios
    a, b, z, angle = generate_valid_params()

    # Calcular coordenadas con funciones trigonométricas
    x = width // 2 + int(100 * (a + z) * math.cos(angle))
    y = height // 2 + int(100 * (b + z) * math.sin(angle))

    # Calcular el color basado en los parámetros
    color = pygame.Color(int(a * 255) % 255, int(b * 155) % 255, int(z * 55) % 255)

    # Dibujar un círculo con el color calculado
    radius = np.random.randint(10, 50)
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()

pygame.quit()
