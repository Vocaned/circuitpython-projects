import board
import adafruit_dht
import time

in_sensor = adafruit_dht.DHT22(board.GP21)
out_sensor = adafruit_dht.DHT22(board.GP22)
while True:
    print(f'Inside temp: {in_sensor.temperature}°C')
    print(f'Outside temp: {out_sensor.temperature}°C')
    time.sleep(10)
