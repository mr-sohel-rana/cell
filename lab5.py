from math import floor

# Question (a)
total_city_coverage_area = 1300  # Total coverage area in square kilometers
radius = 4  # Radius of each cell in kilometers
a = (2.591 * radius ** 2)  # Area covered by each cell
Nc = round(total_city_coverage_area / a)  # Total number of cells, Nc
print(f'(a) Total number of cells, Nc: {Nc} cells\n')

# Question (b)
allocated_spectrum = 40000  # Allocated spectrum in kHz (40 MHz)
channel_width = 60  # Full duplex channel bandwidth in kHz
N = 7  # Reuse factor
C = round(allocated_spectrum / (channel_width * N))  # Total number of channels per cell
print(f'(b) The total number of channels per cell, C: {C} channels/cell\n')

# Question (c)
A = 84  # Traffic intensity per cell from Erlang B chart
print(f'(c) Traffic intensity per cell, A: {A} Erlangs/cell\n')

# Question (d)
max_c_t = floor(Nc * A)  # Maximum carried traffic
print(f'(d) Maximum carried traffic: {max_c_t} Erlangs\n')

# Question (e)
U = round(max_c_t / 0.03)  # Traffic per user, Au = 0.03
print(f'(e) Total number of users, U: {U} users\n')

# Question (f)
no_of_channel = floor(allocated_spectrum / channel_width)  # Total number of channels
no_of_m_p_c = floor(U / no_of_channel)  # Number of mobiles per channel
print(f'(f) Number of mobiles per channel: {no_of_m_p_c} mobiles/channel\n')

# Question (g)
g = C * Nc  # Theoretical maximum number of users that could be served
print(f'(g) Theoretical maximum number of users that could be served: {g} users\n')
