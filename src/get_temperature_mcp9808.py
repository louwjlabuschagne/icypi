from icypi.sensor import Sensor

sensor = Sensor('MCP9808')

print(sensor.get_temperature())