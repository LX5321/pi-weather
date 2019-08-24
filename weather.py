# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# essential os operations
import os
# timing library
import time
# DHT22 Library
import Adafruit_DHT

# intitialise
DHT_SENSOR = Adafruit_DHT.DHT22
# connected DHT22 to pin 4 of raspberry pi
DHT_PIN = 4

try:
#     open file in append mode
#     Write to DB instead of CSV on local machine.  
    f = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
            f.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
#   record humidity and temprature
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

#   data validation check
    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
    else:
#       error
        print("Failed to retrieve data from humidity sensor")

##########################
#  rainwater sensor test #
##########################
     
    no_rain = InputDevice(18)
    if not no_rain.is_active:
        print("It's raining!")
        # insert other code or functions here
        # e.g. tweet, SMS, email, take a photo etc.

    time.sleep(30)       
