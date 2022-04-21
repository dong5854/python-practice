import concurrent.futures
import threading
import redis
import time

conn = redis.Redis(host='localhost', port=6379, db=0)


def run_pubsub():
    # channels = ['idcard_channel', 'driver_channel', 'passport_overseas_channel', 'passport_channel']

    # publish
    threading.Thread(target=publisher, args=(10, 'idcard_channel')).start()
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(publisher, [10 for _ in range(len(channels))], channels)

    # subscribe
    pubsub = conn.pubsub()
    pubsub.subscribe(['idcard_channel'])

    while True:
        print("waiting message...")
        res = pubsub.get_message()
        if res is not None:
            print(res)

        time.sleep(0.5)


def publisher(n: int, channel: str):
    time.sleep(1)
    for num in range(n):
        time.sleep(1)
        conn.publish(channel=f'{channel}', message=f'python pub/sub idcard => {num}')


if __name__ == '__main__':
    run_pubsub()
