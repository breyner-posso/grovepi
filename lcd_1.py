# lcd_1.py
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

while True:
    try:

        setText('Bienvenidos al Curso MDS')
        sleep(1)
        
        #setText_norefresh('Bienvenidos al Curso MDS')
        #sleep(1)

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