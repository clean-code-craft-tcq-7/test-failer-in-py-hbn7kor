def sensorStub():
    return {"temperatureInC": 50, "precipitation": 70, "humidity": 26, "windSpeedKMPH": 52}


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings["temperatureInC"] > 25:
        if readings["precipitation"] >= 20 and readings["precipitation"] < 60:
            weather = "Partly Cloudy"
        elif readings["windSpeedKMPH"] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
