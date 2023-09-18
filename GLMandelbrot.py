import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np
import sys
import joblib

# Configuración de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Conjunto de Mandelbrot en 3D")

# Parámetros para calcular el Conjunto de Mandelbrot
x_min_mandelbrot, x_max_mandelbrot = -2.0, 1.0
y_min_mandelbrot, y_max_mandelbrot = -1.5, 1.5
max_iterations_mandelbrot = 256

# Variables de la cámara
rotation_x = 0
rotation_y = 0
zoom = 1.0

# Función para calcular y dibujar el Conjunto de Mandelbrot en 3D
def calculate_and_draw_mandelbrot():
    glPushMatrix()
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    glScalef(zoom, zoom, zoom)
    glTranslatef(0, 0, -1.0)

    mandelbrot_data = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            zx, zy = x * (x_max_mandelbrot - x_min_mandelbrot) / (WIDTH - 1) + x_min_mandelbrot, \
                     y * (y_max_mandelbrot - y_min_mandelbrot) / (HEIGHT - 1) + y_min_mandelbrot
            c = zx + zy * 1j
            z = c

            for i in range(max_iterations_mandelbrot):
                if abs(z) > 2.0:
                    break
                z = z * z + c
                mandelbrot_data[x, y, :] = (i % 8 * 32, i % 16 * 16, i % 32 * 8)

    glPopMatrix()
    pygame.display.flip()
    return mandelbrot_data

# Configuración de OpenGL
glClearColor(0, 0, 0, 1)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

cache_file = 'mandelbrot_cache.pkl'

try:
    mandelbrot_data = joblib.load(cache_file)
except FileNotFoundError:
    mandelbrot_data = calculate_and_draw_mandelbrot()
    joblib.dump(mandelbrot_data, cache_file)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotation_y += 1
                print(rotation_y)
            elif event.key == pygame.K_RIGHT:
                rotation_y -= 1
                print(rotation_y)
            elif event.key == pygame.K_UP:
                rotation_x += 1
                print(rotation_x)
            elif event.key == pygame.K_DOWN:
                rotation_x -= 1
                print(rotation_x)
            elif event.key == pygame.K_PLUS:
                zoom += 0.1
                print(zoom)
            elif event.key == pygame.K_MINUS:
                zoom -= 0.1
                print(zoom)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Dibuja el conjunto de Mandelbrot desde los datos en caché
    glBegin(GL_POINTS)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            glColor3ub(*mandelbrot_data[x, y, :])
            glVertex3f(x, y, 0)
            print(x,y)
    glEnd()

    pygame.display.flip()

pygame.quit()
sys.exit()
