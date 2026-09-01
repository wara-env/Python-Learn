from flask import Flask, render_template
import random
import time

app = Flask(__name__)


def generate_telemetry():
    temperature = round(random.uniform(25, 40), 2)
    battery_voltage = round(random.uniform(11.5, 12.6), 2)
    battery_current = round(random.uniform(0.5, 2.5), 2)
    altitude = round(random.uniform(100, 500), 2)

    latitude = -7.2756 + random.uniform(-0.001, 0.001)
    longitude = 112.7947 + random.uniform(-0.001, 0.001)

    solar_voltage = round(random.uniform(14, 20), 2)

    if battery_voltage > 11.8:
        system_status = "NORMAL"
    else:
        system_status = "WARNING"

    return {
        "temperature": temperature,
        "battery_voltage": battery_voltage,
        "battery_current": battery_current,
        "altitude": altitude,
        "latitude": round(latitude, 6),
        "longitude": round(longitude, 6),
        "solar_voltage": solar_voltage,
        "system_status": system_status,
        "timestamp": time.strftime("%H:%M:%S")
    }


@app.route("/")
def dashboard():
    telemetry = generate_telemetry()

    return render_template(
        "index.html",
        telemetry=telemetry
    )


if __name__ == "__main__":
    app.run(debug=True)