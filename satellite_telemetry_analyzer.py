import random
import csv
from datetime import datetime


# ==========================================
# MINI SATELLITE TELEMETRY ANALYZER
# ==========================================

def generate_telemetry():
    """Generate simulated satellite telemetry data."""

    telemetry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(-20, 70), 2),
        "battery_voltage": round(random.uniform(10.5, 12.6), 2),
        "battery_current": round(random.uniform(0.5, 3.0), 2),
        "altitude": round(random.uniform(400, 550), 2),
        "signal_strength": random.randint(-100, -50),
        "solar_voltage": round(random.uniform(0, 20), 2)
    }

    return telemetry


def check_status(telemetry):
    """Check satellite condition based on telemetry."""

    warnings = []

    if telemetry["temperature"] > 60:
        warnings.append("High temperature")

    if telemetry["temperature"] < -10:
        warnings.append("Low temperature")

    if telemetry["battery_voltage"] < 11.0:
        warnings.append("Low battery voltage")

    if telemetry["signal_strength"] < -85:
        warnings.append("Weak signal")

    if telemetry["solar_voltage"] < 5:
        warnings.append("Low solar voltage")

    if len(warnings) == 0:
        status = "NORMAL"
    elif len(warnings) <= 2:
        status = "WARNING"
    else:
        status = "CRITICAL"

    return status, warnings


def display_telemetry(telemetry, status, warnings):
    """Display telemetry data."""

    print("\n======================================")
    print("       SATELLITE TELEMETRY")
    print("======================================")

    print(f"Timestamp        : {telemetry['timestamp']}")
    print(f"Temperature      : {telemetry['temperature']} °C")
    print(f"Battery Voltage  : {telemetry['battery_voltage']} V")
    print(f"Battery Current  : {telemetry['battery_current']} A")
    print(f"Altitude         : {telemetry['altitude']} km")
    print(f"Signal Strength  : {telemetry['signal_strength']} dBm")
    print(f"Solar Voltage    : {telemetry['solar_voltage']} V")

    print("--------------------------------------")
    print(f"System Status    : {status}")

    if warnings:
        print("Warnings:")

        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Warnings         : None")

    print("======================================\n")


def save_to_csv(telemetry, status):
    """Save telemetry data to CSV."""

    filename = "telemetry_data.csv"

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            telemetry["timestamp"],
            telemetry["temperature"],
            telemetry["battery_voltage"],
            telemetry["battery_current"],
            telemetry["altitude"],
            telemetry["signal_strength"],
            telemetry["solar_voltage"],
            status
        ])


def main():

    print("🚀 Mini Satellite Telemetry Analyzer")
    print("Starting telemetry system...")

    telemetry = generate_telemetry()

    status, warnings = check_status(telemetry)

    display_telemetry(
        telemetry,
        status,
        warnings
    )

    save_to_csv(
        telemetry,
        status
    )

    print("Telemetry data saved.")


if __name__ == "__main__":
    main()