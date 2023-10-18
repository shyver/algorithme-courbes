import matplotlib.pyplot as plt
import numpy as np
x = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360]
y = [0, 11,37,47.5,50,50,50,50,50,50,50,50,50,50,50,49,41,19,0]
# Calculate dx/dθ = f(θ)
dx_dtheta = np.diff(y) / np.diff(x)
# Smooth the data for plotting
x_smooth = np.linspace(min(x), max(x), 500)  # Generate 500 data points
y_smooth = np.interp(x_smooth, x, y)
plt.plot(x_smooth, y_smooth, label='', color='blue', linestyle='-', linewidth=2)
plt.xlabel('θ-Axis')
plt.ylabel('x-Axis')
plt.title('-Came excentrique à galet-')
plt.grid(True)
plt.legend()
highlight_indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
highlight_x = [x[i] for i in highlight_indices]
highlight_y = [y[i] for i in highlight_indices]
plt.scatter(highlight_x, highlight_y, color='blue', label='Highlighted Points', s=25, marker='o')
plt.yticks(y, y)
plt.xticks(x, x)
print(dx_dtheta)
# Plot the derivative dx/dθ
plt.figure()
plt.plot(x[:-1], dx_dtheta, label='dx/dθ', color='red', linestyle='-', linewidth=2)
plt.xlabel('θ-Axis')
plt.ylabel('dx/dθ')
plt.title('Derivative of x with respect to θ')
plt.grid(True)
plt.legend()
plt.show()
