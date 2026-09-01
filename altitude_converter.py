def meter_to_kilometer(meter):
    return meter / 1000


altitude = float(input("Altitude (m): "))

result = meter_to_kilometer(altitude)

print("Altitude:", result, "km")