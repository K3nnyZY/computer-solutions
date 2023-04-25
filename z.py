import numpy as np

# Parámetros del problema
m = 0.11  # masa (kg)
v0 = 8.0  # velocidad inicial (m/s)
g = 9.8  # aceleración debido a la gravedad (m/s^2)
k = 0.002  # coeficiente de resistencia del aire (kg/m)

# Función que describe la ecuación diferencial
def dvdt(v, t):
    return -g - k * v * abs(v) / m

# Método de Euler para resolver la ecuación diferencial
def euler(dvdt, v0, timesteps):
    v = np.zeros(len(timesteps))
    v[0] = v0
    for i in range(1, len(timesteps)):
        dt = timesteps[i] - timesteps[i - 1]
        v[i] = v[i - 1] + dvdt(v[i - 1], timesteps[i - 1]) * dt
    return v

# Tiempos en los que queremos calcular la velocidad
timesteps = np.arange(0.1, 1.1, 0.1)

# Resolvemos la ecuación diferencial usando el método de Euler
velocities = euler(dvdt, v0, timesteps)

# Imprimimos las velocidades en los tiempos especificados
for t, v in zip(timesteps, velocities):
    print(f"t = {t:.1f} s, v = {v:.2f} m/s")

# Determinamos cuándo el proyectil alcanza su altura máxima y comienza a caer
for i in range(1, len(timesteps)):
    if velocities[i] < velocities[i - 1]:
        t_max_height = timesteps[i - 1]
        break

print(f"El proyectil alcanza su altura máxima y comienza a caer a los {t_max_height:.1f} s")
