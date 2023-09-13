import pygame
import math

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mandala")

# Función de mapeo para ajustar valores a un rango específico
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

# Función que calcula el conjunto de Mandelbrot para un punto dado
def mandelbrot(c):
    z = c
    n = 0
    max_iterations = 100

    while abs(z) <= 2 and n < max_iterations:
        z = z * z + c
        n += 1

    return n / max_iterations

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(width):
        for y in range(height):
            # Calcular valores de Mandelbrot para diferentes puntos
            a = mandelbrot(complex(x / width * 3 - 2, y / height * 3 - 1.5))
            b = mandelbrot(complex(x / width * 3 - 1.8, y / height * 3 - 1.2))
            z = mandelbrot(complex(x / width * 3 - 1.6, y / height * 3 - 1.8))

            # Ajustar valores al rango válido (0-255)
            a = int(map_value(a, 0, 1, 0, 255))
            b = int(map_value(b, 0, 1, 0, 255))
            z = int(map_value(z, 0, 1, 0, 255))

            # Dibujar píxel en pantalla con el color calculado
            color = pygame.Color(a, b, z)
            screen.set_at((x, y), color)

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
