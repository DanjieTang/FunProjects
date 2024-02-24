# script1.py
import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

channel_name = 'communication_channel'

while True:
    message = input("Enter a message: ")
    # Publish message to the channel
    r.publish(channel_name, message)
    time.sleep(1)
