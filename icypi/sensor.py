SUPPORTED_SENSOR_TYPES = ['pi']

class Sensor(object):
    def __init__(self, sensor_type, ip_address, username, password):
        """
        Sensor is an abstraction object for a sensor that can read temperature

        Parameters
        sensor_type(str): Currently on 'pi' is supported
        ip_address(str): IP location of the Pi on the network
        username(str): username to ssh into the pi
        password(str): password associated with username to ssh into the Pi
        """
        assert sensor_type in SUPPORTED_SENSOR_TYPES, f'{sensor_type} is not supported'

        self.sensor_type = sensor_type
        self.ip_address = ip_address
        self.username = username
        self.password = password
        



    def get_temperature(self):
        pass

    def get_sensor_type(self):
        return self.sensor_type
