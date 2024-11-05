import math

# Constants
pt = 50  # Transmitted power in watts
fc = 900  # Carrier frequency in MHz
gt = 1  # Transmitter antenna gain
gr = 1  # Receiver antenna gain
d = 100  # Free space distance in meters
L = 1  # System loss factor

# Calculate wavelength (lambda)
lambda_ = (3 * 10**8) / (fc * 10**6)  # Convert MHz to Hz for frequency

# Question (a)
tr_dBm = math.ceil(10 * math.log10(pt * 1000))  # Convert to dBm
print(f'(a) Transmitter power, Pt in dBm: {tr_dBm} dBm\n')

# Question (b)
tr_dBW = math.ceil(10 * math.log10(pt * 1))  # Convert to dBW
print(f'(b) Transmitter power, Pt in dBW: {tr_dBW} dBW\n')

# Question (c)
c = (pt * gt * gr * (lambda_**2)) / ((4 * math.pi)**2 * (d**2) * L)  # Calculate received power
Pr = 10 * math.log10(c * 1000)  # Convert to dBm
print(f'(c) Received power, Pr in dBm: {Pr:.2f} dBm\n')

# Question (d)
d_10km = Pr + (20 * math.log10(10 * 1000 / 10000))  # Received power at 10 km
print(f'(d) Received power, Pr at 10 km in dBm: {d_10km:.2f} dBm\n')
