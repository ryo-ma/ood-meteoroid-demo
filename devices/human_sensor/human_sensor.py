import RPi.GPIO as GPIO
import time
import json
import argparse
from orion_client import OrionClient


PIN_ID = 14


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_ID, GPIO.IN)


def main(endpoint):
    try:
        current_status = 'ON'
        while True:
            realtime_status = 'ON' if GPIO.input(PIN_ID) == GPIO.HIGH else 'OFF'
            if current_status != realtime_status:
                data = {
                    'status': {
                        'value': realtime_status,
                        'type': 'string'
                    }
                }
                orion_client = OrionClient(endpoint)
                orion_client.patch_attr('HumanSensor1', json.dumps(data))
                print(realtime_status)
                if realtime_status == 'ON':
                    time.sleep(2.5)
            current_status = realtime_status
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="human_sensor.py", description="Human sensor", add_help = True)
    parser.add_argument("endpoint", help="Orion endpoint")
    args = parser.parse_args()
    setup()
    main(args.endpoint)
