import requests
import json


def main(args):
    state = args['data'][0]['status']['value']
    led_endpoint = args['led_endpoint']
    slack_url = args['slack_url']
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
    led_url = '{}/control_led'.format(led_endpoint)
    response = requests.post(led_url, headers=headers, data=json.dumps(data))
    if state == 'ON':
        slack_params = {'channel': '#ood2019',
                       'username': 'webhookbot',
                       'text': '{}のパターンでLEDが光りました'.format(args['pattern']),
                       'icon_emoji': ':ghost:'}
        response = requests.post(slack_url, data=json.dumps(slack_params))
    print(args)
    return {'result': 'success'}
