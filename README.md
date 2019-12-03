# Okinawa Open Days Meteoroid demonstration


## Usage

### Login a raspberry pi with a human sensor

```
ssh user@ip
```

### Start pipenv and Install requirements

```
cd devices/
pipenv shell
pipenv install
```

### Run the human sensor

```
python human_sensor/human_sensor.py http://orion_host:port
```


### Login a raspberry pi with a led

```
ssh user@ip
```


### Start pipenv and Install requirements

```
cd devices/
pipenv shell
pipenv install
```

### Run the led

```
./led/start.sh
```


### Update a function using meteoroid-cli

```
meteoroid function update function_id functions/switch_led.py -p led_endpoint http://host:port -p pattern color_wipe -p color green -l python:3
```
