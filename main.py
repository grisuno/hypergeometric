import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

# Definir la función hipergeométrica generalizada
def hypergeom(a, b, c, z):
    return sp.hyp2f1(a, b, c, z)

# Definir los parámetros 'a', 'b', 'c' y 'z'
a = 1.5
b = 2.5
c = 3.5  # Define el parámetro 'c'
z_values = np.linspace(0, 2, 100)

# Calcular los valores de la función para cada 'z'
result_values = hypergeom(a, b, c, z_values)

# Graficar la función
plt.plot(z_values, result_values, label=f'F({a}, {b}, {c}; z)')
plt.xlabel('z')
plt.ylabel('F(a, b, c; z)')
plt.title('Función Hipergeométrica Generalizada')
plt.legend()
plt.grid(True)
plt.show()
