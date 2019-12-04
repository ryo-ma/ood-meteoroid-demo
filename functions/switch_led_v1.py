import requests
import json


def main(args):
    state = args['data'][0]['status']['value']
    led_endpoint = args['led_endpoint']
    data = {'state': state}
    if 'pattern' in args:
        data['pattern'] = args['pattern']
    if 'color' in args:
        data['color'] = args['color']
    else:
        data['color'] = 'blue'
    headers = {
        'Content-Type': 'application/json'
    }
    url = '{}/control_led'.format(led_endpoint)
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return {'result': 'success'}
