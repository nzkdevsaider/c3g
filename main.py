import numpy as np
import matplotlib.pyplot as plt

# Genera valores para x e y
x = np.linspace(-7, 7, 400)
y = np.linspace(-7, 7, 400)
X, Y = np.meshgrid(x, y)

# Calcula la función sqrt(49 - x^2 - y^2)
Z_values = 49 - X**2 - Y**2
Z_values[Z_values < 0] = 0
Z = np.sqrt(Z_values)

# Coordenadas del punto A
x_a, y_a, z_a = 2, 3, 6

# Ecuación del plano x = 2
x_plane = 2
Z_plane_values = 49 - (x_plane**2) - Y**2
Z_plane_values[Z_plane_values < 0] = 0
Z_plane = np.sqrt(Z_plane_values)

# Intersección de x = 2 con la función principal
x_intersection = np.full_like(Y, x_plane)
y_intersection = Y
z_values = 49 - x_intersection**2 - y_intersection**2
z_values[z_values < 0] = 0
z_intersection = np.sqrt(z_values)

# Crea un gráfico en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grafica la superficie principal con transparencia (alpha=0.5)
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

# Agrega una barra de color
fig.colorbar(surf)

# Etiqueta los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('sqrt(49 - x^2 - y^2)')

# Ubica el punto A
ax.scatter(x_a, y_a, z_a, color='red', label='Punto A (2, 3, 6)')

# Etiqueta el punto A
ax.text(x_a, y_a, z_a, "A (2, 3, 6)", color='red')

# Grafica el plano x = 2
ax.plot_surface(x_intersection, y_intersection, z_intersection, color='green', alpha=0.7, label='x = 2')

# Calcula el gradiente en el punto A
grad_x = -x_a / z_a
grad_y = -y_a / z_a

# Genera valores para t
t = np.linspace(-10, 10, 400)

# Calcula la recta tangente
x_tangent = x_a + t * grad_x
y_tangent = y_a + t * grad_y
z_tangent = z_a + t

# Grafica la recta tangente
ax.plot(x_tangent, y_tangent, z_tangent, color='blue', label='Recta Tangente')

# Muestra el gráfico
plt.legend()
plt.show()
