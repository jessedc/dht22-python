"""
CLI Entry point
"""
import argparse
import time
import Adafruit_DHT
from influxdb import InfluxDBClient
from dht22.influxdb import influx

influx_client = None
influx_db = None


def main():
    """
    Invoke the parser
    :return:
    """
    parser = argparse.ArgumentParser(description='Collect data from dht22 sensor')
    parser.add_argument('-i', '--influx', help='Influx DB host')
    parser.add_argument('-d', '--database', help='InfluxDB database')
    parser.add_argument('-p', '--pin', help='GPIO pin', default=22)
    args = parser.parse_args()

    sensor = Adafruit_DHT.AM2302
    # default value BCM 22, physical pin 15 https://pinout.xyz/pinout/pin15_gpio22
    pin = args.pin

    global influx_db, influx_client
    influx_client = InfluxDBClient(host=args.influx, port=8086)
    influx_db = args.database

    # while loop based on https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
    while True:

        # Try to fetch a sensor reading. Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Note that sometimes you won't get a reading and the results will be null
        # (because Linux can't guarantee the timing of calls to read the sensor).
        if humidity is not None and temperature is not None and humidity < 100:
            print('Temp: {0:0.1f}  Humidity: {1:0.1f}%'.format(temperature, humidity))

            measurements = influx.measurements_for_reading(temperature, humidity)
            influx_client.write_points(measurements, database=influx_db)

        time.sleep(5)


if __name__ == "__main__":
    main()
