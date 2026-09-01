sensor_data = [25, 26, 24, 27, 25]

total = 0

for data in sensor_data:
    total += data

average = total / len(sensor_data)

print("Average:", average)