# http://www.thirdeyevis.com/pi-page-2.php
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import Time library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
for i in range(0,10):
  GPIO.output(7,True) ## Turn on GPIO pin 7
  time.sleep(1)
  GPIO.output(7,True) ## Turn off GPIO pin 7
  time.sleep(1)
