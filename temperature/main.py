import board
import adafruit_dht
import time
import os
import ssl

import socketpool #type: ignore
import wifi #type: ignore

import adafruit_minimqtt.adafruit_minimqtt as MQTT

wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
print(f"Connected to {os.getenv('CIRCUITPY_WIFI_SSID')}!")

pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

mqtt_client = MQTT.MQTT(
    broker=os.getenv("MQTT_BROKER", ""),
    port=int(os.getenv("MQTT_PORT", 0)),
    username=os.getenv("MQTT_USERNAME"),
    password=os.getenv("MQTT_PASSWORD"),
    socket_pool=pool,
    ssl_context=ssl_context,
)
mqtt_client.connect()

dht = adafruit_dht.DHT22(board.GP17)

while True:
    try:
        temp = dht.temperature
        assert temp
        humidity = dht.humidity
        assert humidity
        mqtt_client.publish('home/temperature', temp)
        mqtt_client.publish('home/humidity', humidity)
    except (RuntimeError, AssertionError):
        # Reading sensor failed, retry
        time.sleep(2)
    else:
        time.sleep(30)
