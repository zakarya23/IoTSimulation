import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Got the connection string to connect to the IoT hub. 
CONNECTION_STRING = "HostName=RefridgeratedTruck.azure-devices.net;DeviceId=RefridgeratedTruck1;SharedAccessKey=4kcyBF7QrySX/X5tSdfslV5EqCVwOlUah5DImHypuco="

#Defining the constants to start off with 
TEMPERATURE = 20.0
HUMIDITY = 30
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

def iothub_client_init():
    '''Creates a new IoT client'''
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "Device sending periodic messages" )

        while True:
            # Simulates random values for the temp and humidity and then stores it all in the message variable. 
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
            message = Message(msg_txt_formatted)

            # Generates a random value for variables that cant be generated randomly.
            if temperature > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Prints and then sends of the message to the HUB. 
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
