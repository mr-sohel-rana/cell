import math

# Constants
fc = 1.8  # Frequency in GHz
hb = 20   # Effective transmitter (base station) antenna height in meters

# Calculate the T-R separation distance in kilometers
d = (math.sqrt(20**2 + 30**2)) / 1000  # Convert from meters to kilometers

# Calculate path loss in high-rise urban areas using the given formula
Lp = (135.41 +
      (12.49 * math.log10(fc)) -
      (4.99 * math.log10(hb)) +
      ((46.84 - 2.34 * math.log10(hb)) * math.log10(d)))

# Print the path loss
print(f'The path loss in high-rise urban areas, Lp = {Lp:.2f} dB')
