# buzzer.py
#
# This is an project using the Grove Switch, Buzzer and accelerometer from the GrovePi starter kit
# 
# In this project, the buzzer starts making a sound when the accelerometer is held perpendicular and the Switch is on

'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
'''

import time
from grovepi import *
import math

buzzer_pin = 3      #Port D3 for buzzer
button_pin = 4

pinMode(buzzer_pin,"OUTPUT")    # Assign mode for buzzer as output
pinMode(button_pin,"INPUT")     # Assign mode for button as input

while True:
    try:
        
        button_status= digitalRead(button_pin)
        
        if button_status:
            print('ON')
            digitalWrite(buzzer_pin,1)
            
        else:
            print('OFF')
            digitalWrite(buzzer_pin,0)
        time.sleep(.1)
        
    except KeyboardInterrupt:   # Stop the buzzer before stopping
        digitalWrite(buzzer_pin,0)
        break
    except (IOError,TypeError) as e:
        print("Error")