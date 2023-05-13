# lcd_2.py
#
# This is an project for using the Grove RGB LCD Display.
# - Connect the RGB LCD Display to the I2C Port

from grovepi import *
from grove_rgb_lcd import *
from time import sleep

# set a backlight color
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(255,255,255)
ultrasonic_ranger = 3

while True:
    try:
        
        distancia = ultrasonicRead(ultrasonic_ranger)
        d = str(distancia)
        
        #setText('Distancia ' + d + 'cm')
        setText_norefresh('Distancia ' + d + 'cm')
        
        sleep(0.01)

    except (IOError, TypeError) as e:
        print(str(e))
        # and since we got a type error
        # then reset the LCD's text
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        # since we're exiting the program
        # it's better to leave the LCD with a blank text
        setText("")
        break

    # wait some time before re-updating the LCD
    sleep(0.05)
