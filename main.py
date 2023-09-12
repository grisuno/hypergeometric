import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

# Definir la función hipergeométrica generalizada
def hypergeom(a, b, z):
    return sp.hyp2f1(a, b, z)

# Definir los parámetros 'a', 'b' y 'z'
a = 1.5
b = 2.5
z_values = np.linspace(0, 2, 100)

# Calcular los valores de la función para cada 'z'
result_values = hypergeom(a, b, z_values)

# Graficar la función
plt.plot(z_values, result_values, label=f'F({a}, {b}; z)')
plt.xlabel('z')
plt.ylabel('F(a, b; z)')
plt.title('Función Hipergeométrica Generalizada')
plt.legend()
plt.grid(True)
plt.show()
