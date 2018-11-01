#!/usr/bin/python
import time
import RPi.GPIO as GPIO
delay=0.002
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
ControlPin = [5,6,13,19]

# Set all pins as output
for pin in ControlPin:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, 0)

# Define advanced sequence
# as shown in manufacturers datasheet
seq = [[0,1,0,1],
       [0,1,1,0],
       [1,0,1,0],
       [1,0,0,1]]

for i in range(512):
        for halfstep in range(4):
                for pin in range(4):
                        GPIO.output(ControlPin[pin], seq[halfstep][pin])
                time.sleep(delay)
GPIO.cleanup()