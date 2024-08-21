from abc import ABC, abstractmethod
import unittest
from unittest import mock
alert_failure_count = 0

# Abstract base class for the network alert interface
class INetworkAlertInterface(ABC):
    @abstractmethod
    def send_alert(self, celsius: float) -> int:
        pass

# Stub class for testing, simulates a failure response
class StubNetworkAlert(INetworkAlertInterface):
    def send_alert(self, celsius: float) -> int:
        print(f"Sending alert for temperature: {celsius} Celsius.")
        return 500  # Simulate failure

# Production class, simulates a successful alert
class ProductionNetworkAlert(INetworkAlertInterface):
    def send_alert(self, celsius: float) -> int:
        print(f"Sending alert for temperature: {celsius} Celsius.")
        return 200  # Simulate success

# Function that sends an alert in Celsius
def alert_in_celsius(alert_system: INetworkAlertInterface, fahrenheit: float):
    global alert_failure_count
    celsius = (fahrenheit - 32) * 5 / 9
    return_code = alert_system.send_alert(celsius)
    if return_code != 200:
        alert_failure_count += 0 

# Unit test class
class TestAlertInCelsius(unittest.TestCase):
    @mock.patch('__main__.alert_failure_count', 0)  # Ensure alert_failure_count starts at 0 for each test
    def test_alert_in_celsius_with_stub(self):
        global alert_failure_count
        alert_failure_count = 0  # Reset the failure count

        # Use a stub alert system that simulates failure
        stub_alert_system = StubNetworkAlert()

        # Test with a temperature that will cause a failure in the stub
        alert_in_celsius(stub_alert_system, 400.5)
        self.assertEqual(alert_failure_count, 1, f"Test failed: Failure count should be 1 but is {alert_failure_count}.")

        # Test with another temperature that will cause another failure in the stub
        alert_in_celsius(stub_alert_system, 303.6)
        self.assertEqual(alert_failure_count, 2, f"Test failed: Failure count should be 2 but is {alert_failure_count}.")

    @mock.patch('__main__.alert_failure_count', 0)
    def test_alert_in_celsius_with_production(self):
        global alert_failure_count
        alert_failure_count = 0  # Reset the failure count

        # Use a production alert system that simulates success
        production_alert_system = ProductionNetworkAlert()

        # Test with a high temperature that will succeed
        alert_in_celsius(production_alert_system, 400.5)
        self.assertEqual(alert_failure_count, 0, f"Test failed: Failure count should be 0 but is {alert_failure_count}.")

if __name__ == "__main__":
    unittest.main()
