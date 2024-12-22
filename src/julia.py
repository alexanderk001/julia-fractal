import numpy as np
import matplotlib.pyplot as plt

# Define the Iteration Rule
def my_func(z, c):
    return z**2 +c

# Create the Julia Set
def julia_set(func, c, width, height, zoom, max_iter):
    # Initialize a 2D array to store iteration counts
    julia = np.zeros((width, height))

    # Create ranges for the real and imaginary parts of the complex plane
    x_range = np.linspace(-1.5 * zoom, 1.5 * zoom, width)
    y_range = np.linspace(-1.5 * zoom, 1.5 * zoom, height)

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            zx = x_range[x]
            zy = y_range[y]
            z = complex(zx, zy)
            iteration = 0

            while abs(z) < 2 and iteration < max_iter:
                z = func(z, c)
                iteration += 1

            julia[x, y] = iteration

    return julia

# Set the Parameters
width, height = 800, 800
zoom = 1
c = complex(-0.8, 0.156)
max_iter = 300

# Generate the Julia Set
julia = julia_set(my_func, c, width, height, zoom, max_iter)

# Visualize the Julia Set
plt.figure(figsize=(12, 12))
plt.imshow(julia.T, cmap='inferno', origin='lower', aspect='equal', 
           extent=[-1.5*zoom, 1.5*zoom, -1.5*zoom, 1.5*zoom])
plt.colorbar(label="Iterations")
plt.title(f'Julia Set for c = {c} and $f(z) = z^2 + c$', fontsize=18)
plt.xlabel('Re(z)', fontsize=15)
plt.ylabel('Im(z)', fontsize=15)

# plt.tight_layout()
# plt.savefig('julia_set.png', dpi=600)

plt.show()
