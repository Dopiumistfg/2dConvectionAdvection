import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the update function for the animation
def update(frame):
    # Calculate temperature evolution using finite differences
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):
            # updating vorticity
            Omega[i, j] = Omega[i, j] + dt * (((Psi[i + 1, j] - Psi[i - 1, j]) * (Omega[i, j + 1] - Omega[i, j - 1]) / (4*dx**2) 
                            + (Psi[i, j - 1] - Psi[i, j + 1]) * (Omega[i + 1, j] - Omega[i - 1, j]) / (4*dx**2) 
                            + nu * (Omega[i, j - 1] + Omega[i, j + 1] + Omega[i - 1, j] + Omega[i + 1, j] - 4 * Omega[i, j])/dx**2)
                            -  g * (Temperature[i,j+1]-Temperature[i,j-1])/(2*dx*rho))
            
            
    #updating stream function
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):        
            Psi[i, j] = (Omega[i ,j] * dx**2 + Psi[i, j-1] + Psi[i, j+1] + Psi[i-1, j] + Psi[i+1, j]) / 4.0
            
    #Updating temperature taking u and v with central difference
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):        
            u = (Psi[i, j + 1] + Psi[i, j - 1] - 2*Psi[i,j]) / (dx)
            if forcedconvection:
                v = (Psi[i + 1, j] + Psi[i - 1, j] - 2*Psi[i,j]) / (dx)
            else:
                v = 0
            
            Temperature[i,j] = Temperature[i,j] + dt * ( alpha * (Temperature[i, j - 1] + Temperature[i, j + 1] + Temperature[i - 1, j] + 
                                                                Temperature[i + 1, j] - 4 * Temperature[i, j]) / dx**2 - 
                                                        u*(Temperature[i, j + 1] - Temperature[i, j - 1]) / (2* dx) +
                                                        v*(Temperature[i + 1, j] - Temperature[i - 1, j]) / (2* dx) )
            
    # Update the plot
    plt.clf()
    plt.imshow(Temperature, cmap='coolwarm', interpolation='nearest')
    plt.colorbar()
    plt.title('Temperature at time = {:.3f}'.format(frame*dt))
    plt.xlabel('x')
    plt.ylabel('y')

# defining constants
length = 10
nodes = 101
dx = length / (nodes - 1)
dt = 0.01
nu = 0.1
alpha = 0.1
g = 9.81
rho = 1.224
forcedconvection = False

Psi = np.zeros((nodes, nodes))
Omega = np.zeros((nodes, nodes))
Temperature = np.zeros((nodes, nodes))

PsiOld = np.zeros((nodes, nodes))
OmegaOld = np.zeros((nodes, nodes))
TemperatureOld = np.zeros((nodes, nodes))

# initial conditions
Temperature[-1, :] = 1

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=1000, interval=10, repeat=False)
# Show the animation
plt.show()
print(Psi)