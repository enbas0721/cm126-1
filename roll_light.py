import RPi.GPIO as GPIO
import time
import sys

servo_pin = 18
led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)

servo.start(0)
GPIO.output(17, 1)

def servo_angle(servo, angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    servo.ChangeDutyCycle(duty)

while True:
    try:
        servo_angle(servo, 90)
        time.sleep(3)
        servo_angle(servo, -90)
        time.sleep(3)
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        sys.exit()