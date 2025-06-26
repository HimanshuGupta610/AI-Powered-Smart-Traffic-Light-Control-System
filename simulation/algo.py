def calculate_green_light_time(cars, base_time, time_per_car, max_time):
    n = len(cars)  # Number of lanes
    green_light_time = [0] * n  # Initialize the green light duration for each lane

    # Calculate green light duration based on the number of cars in each lane
    for i in range(n):
        # Calculate time for the lane
        lane_time = int(base_time + (cars[i] * time_per_car)/2)
        
        # Cap the time to avoid overflow
        green_light_time[i] = min(lane_time, max_time)

    return green_light_time

# Example Usage for Four Lanes
lane1 = int(input("No. of cars in lane 1: "))
lane2 = int(input("No. of cars in lane 2: "))
lane3 = int(input("No. of cars in lane 3: "))
lane4 = int(input("No. of cars in lane 4: "))
cars = [lane1, lane2, lane3, lane4]  # Number of cars in the four lanes
base_time = 5  # Base green light duration (in seconds)
time_per_car = 2  # Additional time for each car (in seconds)
max_time = 60  # Maximum green light duration per lane (in seconds)

# Calculate green light durations
green_light_times = calculate_green_light_time(cars, base_time, time_per_car, max_time)

# Print the green light durations for each lane
print("Green light durations for each lane:", green_light_times)
