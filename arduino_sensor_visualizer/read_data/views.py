from django.template import loader
from django.http import HttpResponse
from . import arduino_serial_communication as arduino 
from . import urls


def return_sensor_data(request):
    # return HttpResponse("Hello World")
    my_dict = {'first_name': 'John', 'last_name': 'Doe'}
    print(urls.station_port)
    sensor_data = arduino.read_from_station(urls.station_port)
    
    sensor_data_dict = {'temperature':float(sensor_data[0][1:]),
                        'humidity' : float(sensor_data[1][1:])}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(sensor_data_dict,request))