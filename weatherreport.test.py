import unittest
from unittest.mock import patch
from weatherreport import report, sensorStub


class TestWeatherReport(unittest.TestCase):
    @patch("weatherreport.sensorStub")
    def testSunny(self, sensorstub):
        sensorstub.return_value = {"temperatureInC": 25, "precipitation": 70, "humidity": 26, "windSpeedKMPH": 52}
        self.assertEqual(report(sensorstub), "Sunny Day")

    def testRainy(self):
        self.assertEqual(report(sensorStub), "Alert, Stormy with heavy rain")

    @patch("weatherreport.sensorStub")
    def testCloudy(self, sensorstub):
        sensorstub.return_value = {"temperatureInC": 50, "precipitation": 30, "humidity": 26, "windSpeedKMPH": 52}
        self.assertEqual(report(sensorstub), "Partly Cloudy")


if __name__ == "__main__":
    unittest.main()
