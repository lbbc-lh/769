from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.pubnub import PubNub, SubscribeListener
import picamera
import io
import base64
import time

# pubnub config
config = PNConfiguration()
config.publish_key = "pub-c-9d79be43-60ba-4e51-a889-8a85b4c29509"
config.subscribe_key = "sub-c-31f4e71c-c7ba-46c5-b2a7-661511e01554"
config.uuid = "769channel"
pubnub = PubNub(config)

THRESHOLD = 0

# get data from ultrasonic sensor
# TODO
while False:
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



# camera sensor capture
camera = picamera.PiCamera()
buffer = io.BytesIO()
camera.capture(buffer, format='jpeg')
# get the bytes in the buffer, base64 encode, then decode to string
data = base64.b64encode(buffer.getvalue()).decode()
# close
buffer.close()
camera.close()




# publish data
message = {
    "data": "base64_data",
    "timestamp": time.time()
}
pubnub.publish().channel('769channel').message(message).use_post(True).sync()