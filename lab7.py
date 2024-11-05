import math

# Constants
hte = 100  # Effective transmitter (base station) antenna height in meters
hre = 2    # Effective receiver (mobile) antenna height in meters
fc = 900   # Frequency in MHz
d = 4      # T-R separation distance in kilometers

# Calculate the correction factor using the Okumura-Hata model
a_hre = (3.2 * (math.log10(11.75 * hre)) ** 2) - 4.97

# Calculate path loss in urban areas
Lp = (69.55 +
      26.16 * math.log10(fc) -
      13.82 * math.log10(hte) -
      a_hre +
      ((44.9 - 6.55 * math.log10(hte)) * math.log10(d)))

# Print the path loss
print(f'The path loss in urban areas, Lp = {Lp:.2f} dB')
