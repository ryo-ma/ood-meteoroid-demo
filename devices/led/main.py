from flask import Flask, request, jsonify, Response
from led_controller import LEDController

app = Flask(__name__)
led_controller = LEDController()

@app.route('/control_led', methods=['POST'])
def control_led():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    state = request.json['state']
    if state == 'OFF':
        led_controller.off()
    elif state == 'ON':
        if 'rainbow' in request.json['pattern']:
            led_controller.on_rainbow(request.json['pattern'])
        else:
            led_controller.on(request.json['color'], request.json['pattern'])
    return jsonify(res='success'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
