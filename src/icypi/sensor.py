import Adafruit_MCP9808.MCP9808 as MCP9808
SUPPORTED_SENSOR_TYPES = ['MCP9808']

class Sensor(object):
    def __init__(self, sensor_type):
        """
        Sensor is an abstraction object for a sensor that can read temperature

        Parameters
        sensor_type(str): Currently only 'MCP9808' is supported
        """
        assert sensor_type in SUPPORTED_SENSOR_TYPES, f'{sensor_type} is not supported'

        self.sensor = MCP9808.MCP9808()
        self.sensor_type = sensor_type
  

    def get_temperature(self):
        """
        Function that initialises the sensor 
        and gets the temperature in Celcious

        Return
        temperature (float)
        """
        if self.sensor_type == 'MCP9808':
            self.sensor.begin()
            temp = self.sensor.readTempC()
        else:
            temp = -9999
        return temp

    def get_sensor_type(self):
        return self.sensor_type
