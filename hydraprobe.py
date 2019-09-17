from chirp_modbus import SoilMoistureSensor
s = SoilMoistureSensor(0, '/dev/ttyUSB0')
print(s.getTemperature())
print(s.getMoisture())
