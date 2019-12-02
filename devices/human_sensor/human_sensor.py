import RPi.GPIO as GPIO
import time

PIN_ID = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_ID, GPIO.IN)

current_state = 'ON'


try:
    while True:
        realtime_state = 'ON' if GPIO.input(PIN_ID) == GPIO.HIGH else 'OFF'
        if current_state != realtime_state:
            # TODO: send to Orion
            print('Change ', realtime_state)
            time.sleep(5)
        current_state = realtime_state
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
