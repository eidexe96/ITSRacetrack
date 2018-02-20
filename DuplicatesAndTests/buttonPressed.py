import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, initial=GPIO.LOW)

def buttonPressed()
    return GPIO.input(10)