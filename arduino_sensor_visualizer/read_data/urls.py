from django.urls import path
from . import views
from . import arduino_serial_communication as arduino



available_station_ports = arduino.search_for_available_station_ports()
if available_station_ports == False:
    print("No available arduino ports found!")
    exit()

station_port = arduino.connect_to_station(available_station_ports[0])
if station_port == -1:
    print("device can not be found or can not be configured!")
elif station_port == -2:
    print("parameter are out of range, e.g. baud rate, data bits!")
else:
    print("SUCCESSFULLY CONNECTED TO PORT {}".format(station_port.port))


urlpatterns = [
    path('show', views.return_sensor_data, name='read_data'),
]
