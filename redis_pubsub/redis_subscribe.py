import redis
import time

conn = redis.Redis(host='localhost', port=6379, db=0)

# subscribe
pubsub = conn.pubsub()
pubsub.subscribe(['idcard_channel'])

while True:
    print("waiting message...")
    res = pubsub.get_message()
    if res is not None:
        print(res)
    time.sleep(0.5)
