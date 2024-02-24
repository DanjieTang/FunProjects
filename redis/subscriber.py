# script2.py
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

channel_name = 'communication_channel'

# Subscribe to the channel
pubsub = r.pubsub()
pubsub.subscribe(channel_name)

print(f"Subscribed to {channel_name}. Waiting for messages...")

# Listen for messages
for message in pubsub.listen():
    if message['type'] == 'message':
        data = message['data']
        print(f"Received: {data.decode('utf-8')}")
