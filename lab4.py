# Given data
blocking_probability = 2 / 100  # GOS
population = 2000000
Au = (2 / 60) * 3  # Traffic intensity per user

# System A
print('For system A:')
print('--------------')
C1 = 19  # Number of channels per cell
A1 = 12  # Total traffic intensity from Erlang B chart, GOS=0.02, C=19
U1 = A1 / Au  # Total number of users
Aa = U1 * 394  # Total Number of Subscribers
percentage_A = (Aa / population) * 100

print(f'Total number of users for system A: {int(Aa)}')
print(f'Percentage market penetration for System A: {percentage_A:.3f}%')

print('\n\nFor system B:')
print('--------------')
C2 = 57  # Number of channels per cell
A2 = 45  # Total traffic intensity from Erlang B chart, GOS=0.02, C=57
U2 = A2 / Au  # Total number of users
Bb = U2 * 98  # Total Number of Subscribers
percentage_B = (Bb / population) * 100

print(f'Total number of users for system B: {int(Bb)}')
print(f'Percentage market penetration for System B: {percentage_B:.3f}%')

print('\n\nFor system C:')
print('--------------')
C3 = 100  # Number of channels per cell
A3 = 88  # Total traffic intensity from Erlang B chart, GOS=0.02, C=100
U3 = A3 / Au  # Total number of users
Cc = U3 * 49  # Total Number of Subscribers
percentage_C = (Cc / population) * 100

print(f'Total number of users for system C: {int(Cc)}')
print(f'Percentage market penetration for System C: {percentage_C:.3f}%')

print('\n\nFor all three systems:')
print('--------------------')

T = Aa + Bb + Cc  # Total Subscribers
percentage_T = (T / population) * 100

print(f'Total number of users of all three systems: {int(T)}')
print(f'Percentage market penetration for all three Systems: {percentage_T:.3f}%')
