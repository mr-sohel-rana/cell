import numpy as np

# Given data
GOS = 0.5 / 100  # Grade of Service (blocking probability)
Au = 0.1  # Traffic intensity per user

# Offered Traffic Intensity, A
A = np.array([0.005, 1.13, 3.96, 11.1, 80.9])

# Trunked Channels
C = np.array([1, 5, 10, 20, 100])

# Total number of users
U = np.round(A / Au).astype(int)  # Round to nearest integer

# Result print
print(f'Grade of Service, GOS = {GOS:.3f}')
print('Trunked Channels, C :')
print(C)
print('From table 3.1, we obtain Offered Traffic Intensity, A For all Channels, C :')
print(A)
print('Total number of users, U')
print('---------------------------')
print(U)
