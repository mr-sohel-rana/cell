import math

# Constants
R = 1.387  # Cell Radius in km
n = 4  # Number of cells
N = 60  # Total number of channels
area = round(2.5981 * R**2)  # Area covered per cell in sq km
C = N / 4  # Number of channels per cell
A = 9  # Traffic intensity at C=15, GOS=0.05, Au=0.029 from Erlang C chart

# Question (a)
Au = 0.029  # Traffic per user
U = math.floor(A / Au)  # Number of users
U_per = round(U / area)  # Number of users per square km
print(f'(a) Number of users per square km: {U_per} users/sq km\n')

# Question (b)
lemda = 1  # lambda = 1 hour
H = (Au / lemda) * 3600  # Holding Time from hour to seconds
Prb = math.exp((-(C - A) * 10) / H)  # Probability that a delayed call will have to wait
print(f'(b) The probability that a delayed call will have to wait: {Prb * 100:.2f}%\n')

# Question (c)
Prc = 0.05 * Prb * 100  # 5% probability of delayed call
print(f'(c) The probability that a call will be delayed: {Prc:.2f}%\n')
