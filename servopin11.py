import RPi.GPIO as GPIO
import time
servo_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

pwm=GPIO.PWM(servo_pin,100)
pwm.start(5)

angle1=10
duty1= float(angle1)/10 + 2.5

angle2=160
duty2= float(angle2)/10 + 2.5

ck=0
while ck<=5:
     pwm.ChangeDutyCycle(duty1)
     time.sleep(0.8)
     pwm.ChangeDutyCycle(duty2)
     time.sleep(0.8)
     ck=ck+1
time.sleep(1)
pwm.stop()
GPIO.cleanup()