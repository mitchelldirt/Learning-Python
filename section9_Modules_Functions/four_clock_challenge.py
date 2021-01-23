# Python program to explain time.get_clock_info() method

# importing time module
import time

# Clock name
clock_name = 'monotonic'

# Get the information on
# the specified clock name
clock_info = time.get_clock_info(clock_name)

# Print the information
print("Information on '% s':" % clock_name)
print(clock_info)

clock_name = 'perf_counter'

# Get the information on
# the specified clock name
clock_info = time.get_clock_info(clock_name)

# Print the information
print("\nInformation on '% s':" % clock_name)
print(clock_info)

clock_name = 'process_time'

# Get the information on
# the specified clock name
clock_info = time.get_clock_info(clock_name)

# Print the information
print("\nInformation on '% s':" % clock_name)
print(clock_info)

clock_name = 'time'

# Get the information on
# the specified clock name
clock_info = time.get_clock_info(clock_name)

# Print the information
print("\nInformation on '% s':" % clock_name)
print(clock_info)

