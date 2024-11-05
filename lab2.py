import math

def calculate_cluster_size_and_sir(pl_exponent, r_si=15, i0=6):
    for n in pl_exponent:
        N = 7  # Initial cluster size

        # Calculate initial results
        Q = math.sqrt(3 * N)  # Frequency reuse factor
        si = 10 * (math.log10((Q ** n) / i0))  # Signal to interference ratio in dB

        # If initial condition is not satisfied
        if si < r_si:
            i = 2
            j = 2
            N = (i * i) + (i * j) + (j * j)  # Calculate new N for 12-cell reuse
            Q = math.sqrt(3 * N)
            si = 10 * (math.log10((Q ** n) / i0))

        # Result print
        print(f'For Path Loss Exponent, n = {n}')
        print('---------------------------')
        print(f'Signal-to-Noise interference Ratio S/I: {si:.3f} dB > {r_si} dB')
        print('Hence, Cluster size N:')
        print(f': {N}')
        print('Frequency Reuse Factor Q:')
        print(f': {Q:.3f}')
        print()  # Print a newline for better separation between outputs


# Input: Enter path loss exponents
input_exponents = input("Enter Path Loss exponent with [ ] around them: ")
path_loss_exponents = [int(n) for n in input_exponents.strip("[]").split()]

# Calculate and display results
calculate_cluster_size_and_sir(path_loss_exponents)
