'''
1.Function search_for_available_station_ports() returns list of the names of all available station ports on given computer.
    If no available station ports are found then it returns False. 

2.Function connect_to_station(port_name) is used to connect to the station.
    It returns Serialo object.

3.Functioin check_is_port_connected(device_port,time_interval). 
    It is run in diamon thread and is responsible for  checking at equal time intervals(<time_interval>) for if the port was closed.


4.Function write_data(datastring,station_port_object) - tell the station some data.Returns  False if data wasn't written successfully.

5. Functioin read_data(station_port) - this function returns the data read or False if data wasn't read successfully.
'''

'''
error codes:


-2 = Port is disconnected
'''

from time import sleep
import serial.tools.list_ports 
import threading
from os import _exit

STATION_MANUFACTURER = "arduino"
BAUDRATE = 9600
TIMEOUT = 1
PORT_CHECK_TIME_INTERVAL = 0.4


class PortDisconnected(Exception):
    pass


def search_for_available_station_ports():
    try:
        ports = serial.tools.list_ports.comports()
        available_arduino_ports = []
        any_arduino_ports = False
        # print("LIST AVAILABLE PORTS")
        for port in ports:
            # print("Name: {}".format(ports[i].name))
            # print("Manufacturer: {}".format(ports[i].manufacturer))
            # print("Description: {}".format(ports[i].description))
            # print("----------------------------------------") 
            if STATION_MANUFACTURER in port.manufacturer.lower():
                available_arduino_ports.append(port.device)
                any_arduino_ports = True
        if any_arduino_ports:
            return available_arduino_ports
        else:
            return False
    except AttributeError:
        return -2
        # _exit()

def connect_to_station(device_port):
    try:
        port = serial.Serial(port=device_port,baudrate=BAUDRATE,timeout=TIMEOUT)
        port_thread = threading.Thread(target=check_is_port_connected,args=(device_port,PORT_CHECK_TIME_INTERVAL))
        port_thread.daemon = True
        port_thread.start()
        print("Started port_checking daemon!")
        # print("The port is: {}".format(port))
        return port
    # except serial.SerialException:
    #     return -1
    except ValueError:
        return -2
    

def check_is_port_connected(device_port,time_interval):
    # print(device_port)
    # print(type(device_port))
    try:
        while True:
            # print(device_port)s
            available_ports = search_for_available_station_ports()
            if available_ports == False or device_port not in available_ports:
                # print("Port disconnected!")
                raise PortDisconnected
            # for port in device_port:
            #     if port not in available_ports:
                    
                
            sleep(time_interval)
    except PortDisconnected:
        # print("Terminating program...")
        # _exit(0)
        return -1

def write_data_port(text_data,station_port):
    encoded_data = text_data.encode('utf-8')
    print(type(station_port))
    num_byes_written = station_port.write(encoded_data)
    if len(encoded_data) == num_byes_written:
        return True
    else:
        return False

def read_data_port(station_port):
    received_data = ""
    if station_port.in_waiting:
        while station_port.in_waiting:
            received_data += station_port.read().decode('utf-8')
            sleep(0.1)
        # print("Data: " + received_data)
    return received_data

def write_to_station(text_data,station_port):
    if write_data_port(text_data,station_port) == True:
        # print("Data sent successfully!")
        sleep(0.7)
        received_data = read_data_port(station_port)
        # print(received_data)
        if received_data == text_data:
            # print("Data recieved successfullly!!:)")
            return True
        else:
            # print("Data was NOT RECEIVED SUCCESSFULLY!")
            return False
        # return True
    else:
        # print("Data was NOT sent successfully.")
        return False
    

def read_from_station(station_port):
    if write_data_port("R",station_port):
        # print("Data was sent successfully!")
        sleep(1)
        received_data = read_data_port(station_port)[1:]
        print("Received data: " + received_data)
        received_data = received_data.split(';')
        temperature = float(received_data[0][1:])
        humidity = float(received_data[1][1:])
        print("Temp: " + str(temperature))
        print("Hum: " + str(humidity))
        return received_data
    else:
        # print("Data was NOT sent successfully!")
        return False
        

# def write_measurments(text_data,station_port):
#     encoded_data = text_data.encode('utf-8')
#     print(type(station_port))
#     num_byes_written = station_port.write(encoded_data)
#     if len(encoded_data) == num_byes_written:
#         print("Successfully sent data")
#         sleep(0.6)
#         # received_data = ""
#         # if station_port.in_waiting:
#         #     while station_port.in_waiting:
#         #         received_data += station_port.read().decode('utf-8')
#         received_data = read_data(station_port)
#         print("From write received: " + received_data)
#         if received_data == text_data:
#             print("The data was received successfully")
#         else:
#             print("The data WAS NOT received successfully!")
#     else:
#         print("Data wasn't sent correctly!!")

# def read_data(station_port):
#     received_data = ""
#     if station_port.in_waiting:
#         while station_port.in_waiting:
#             received_data += station_port.read().decode('utf-8')
#         print("Data: " + received_data)
#     return received_data


# print("Working!")

if __name__ == "__main__":
    available_station_ports = search_for_available_station_ports()
    if available_station_ports == False:
        print("No available arduino ports found!")
        exit()

    station_port = connect_to_station(available_station_ports[0])
    if station_port == -1:
        print("device can not be found or can not be configured!")
    elif station_port == -2:
        print("parameter are out of range, e.g. baud rate, data bits!")
    else:
        print("SUCCESSFULLY CONNECTED TO PORT {}".format(station_port.port))

    print("Unplug it!")
    sleep(2)
    write_to_station("Test",station_port)
    read_from_station(station_port)
# Debug prompt
# write_data("R",station_port)
# print(f"Received data: {read_data(station_port,option=2)}")
# while True:
#     print("Running..")
#     sleep(0.4)
