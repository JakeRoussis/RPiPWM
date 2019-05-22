import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# Declare pins
pinTrig = 8
pinEcho = 10
pinLED = 11

# Set-up Pins
GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(pinLED, GPIO.OUT)

# Declare pwm pin/variable
pwm = GPIO.PWM(pinLED, 100)
pwm.start(0)

# Enter loop
while True:
    # Trigger sensor
    GPIO.output(pinTrig, True)
    time.sleep(0.00001)
    GPIO.output(pinTrig, False)

    # Sensor start recording
    while GPIO.input(pinEcho) == 0:
        pulse_start = time.time()
        
    # Sensor stop recording
    while GPIO.input(pinEcho) == 1:
        pulse_end = time.time()

    # Calculate distance & print
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distance:", distance, "cm")
    
    # Get value for PWM
    pwmVal = round(distance, 0)
    
    # Check if pwmVal is within range. Limited to 100cm
    if (pwmVal < 100):
        pwm.ChangeDutyCycle(pwmVal)    
    else:
        pwmVal = 100
        pwm.ChangeDutyCycle(pwmVal)
        
    time.sleep(1)
    
# Close script, free resources
GPIO.output(pinTrig, False)
GPIO.cleanup()
