# Adjust LED brightness by rotating Potentiometer

# GrovePi + Rotary Angle Sensor (Potentiometer) + LED
# http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit

'''
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
THE SOFTWARE.
'''

import time
import grovepi

# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

# Connect the LED to digital port D3
led = 3

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        # Read resistance from Potentiometer
        i = grovepi.analogRead(potentiometer)
        print(i)

        # Send PWM signal to LED
        grovepi.analogWrite(led,i//4)
        b= i//4
        print(b)
        
        time.sleep(1)

    except IOError:
        print("Error")
