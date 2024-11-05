import math

# Constants
f = 900  # Frequency in MHz
g = 2.55  # Gain of antenna in dB

# Question (a)
gain = 10 ** (g / 10)
lemda = (3 * 10**8) / (f * 10**6)  # Wavelength in meters
L = lemda / 4  # Antenna Length

print('For (a)')
print('---------')
print(f'Length of the antenna: {L:.3f} m')
print(f'Gain of the antenna: {gain:.1f} = {g:.2f} dB\n')

# Question (b)
print('For (b)')
print('---------')
d = 5000  # T-R separation distance in meters
E0 = 10 ** -3  # Electric-field in V/m
d0 = 1000  # Transmitter distance in meters
ht = 50  # Transmitting antenna height in meters
hr = 1.5  # Receiving antenna height in meters

# Electric Field calculation
Er_d = (2 * E0 * d0 * 2 * math.pi * ht * hr) / (lemda * d**2)

# Effective Aperture calculation
Ae = (gain * lemda**2) / (4 * math.pi)

# Received power at a distance d
Pr_d = (Er_d**2 / (120 * math.pi)) * Ae
Pr_dB = 10 * math.log10(Pr_d)

print(f'Electric Field, Er(d): {Er_d:.9f} V/m')
print(f'Effective Aperture, Ae: {Ae:.3f} m^2')
print(f'Received power at 5 km distance Er(5 km): {Pr_dB:.3f} dBW')
