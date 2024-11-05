def compute_channels(reuse_factor):
    total_bandwidth_khz = 33000  # Total bandwidth in kHz (33 MHz)
    duplex_channel_bandwidth_khz = 50  # 50 kHz per duplex channel
    control_bandwidth_khz = 1000  # 1 MHz (1000 kHz) dedicated to control channels

    # Total available channels
    total_channels = total_bandwidth_khz // duplex_channel_bandwidth_khz

    # Number of control channels
    control_channels = control_bandwidth_khz // duplex_channel_bandwidth_khz

    # Total number of channels available per cell
    channels_per_cell = total_channels // reuse_factor

    # Number of voice channels per cell
    voice_channels_per_cell = (total_channels - control_channels) // reuse_factor

    # Number of control channels per cell
    control_channels_per_cell = channels_per_cell - voice_channels_per_cell

    return channels_per_cell, voice_channels_per_cell, control_channels_per_cell


# Input: Enter cluster sizes
input_clusters = input("Enter Cluster Sizes with [ ] around them: ")
reuse_factors = [int(n) for n in input_clusters.strip("[]").split()]

# Output format
for reuse_factor in reuse_factors:
    total_channels, voice_channels, control_channels = compute_channels(reuse_factor)
    print(f"For Cluster size N = {reuse_factor}")
    print(f"Total number of channels available per cell   : {total_channels} channels")
    print(f"Voice Channels per Cell                        : {voice_channels} channels")
    print(f"Control Channels per Cell                      : {control_channels} channels")
    print()
