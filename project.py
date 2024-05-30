from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time

# pubnub config
config = PNConfiguration()
config.publish_key = "pub-c-9d79be43-60ba-4e51-a889-8a85b4c29509"
config.subscribe_key = "sub-c-31f4e71c-c7ba-46c5-b2a7-661511e01554"
config.user_id = "769"
pubnub = PubNub(config)

THRESHOLD = 0

# get data from ultrasonic sensor
# TODO
while True:
    distance = 0

    # trigger the buzzer and get data from camera sensor
    if distance < THRESHOLD:
        # buzzer
        # TODO

        # get data from camera sensor
        # TODO

        # convert to base64
        # TODO

        # publish data
        camera_sensor_data = {
            "data": "base64_data",
            "timestamp": time.time()
        }
        pubnub.publish().channel('camera_sensor').message(camera_sensor_data).use_post(True)

