import random
import time

from azure.iot.device import IoTHubDeviceClient, Message

# Device authentication string to connect to the IoT hub
CONNECTION_STRING = "HostName=smart-farm.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=1LzgWmvJIEKjgFEMq7Uw0KyDMBTanQHeVK0OeFLO20Q="

# Define the constants to start off with and the message that will be printed out 
TEMPERATURE = 20.0
HUMIDITY = 60
MOISTURE = 5 
MSG_TXT = '{{"Temperature": {temperature} ,"Humidity": {humidity}, "Moisture": {moisture}, "Time": {time}}}'

def iothub_client_init():
    # Creates an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():
    timeTaken = 0 
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Building the message
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            moisture = MOISTURE + (random.random() * 20)
            timeTaken +=0.1 
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity, moisture=moisture, time=timeTaken)
            message = Message(msg_txt_formatted)

            # Add a warning message if temp goes above the required limit set
            if temperature > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Sends the message.
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
