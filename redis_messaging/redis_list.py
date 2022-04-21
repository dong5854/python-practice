import threading
import redis
import time

conn = redis.Redis(host='localhost', port=6379, db=0)


def run_list_queue():

    # sender
    threading.Thread(target=sender, args=(10,)).start()

    # receiver
    while True:
        print("waiting message...")
        res = conn.blpop('test_list', timeout=0)
        if res is not None:
            print(res)
        time.sleep(0.5)


def sender(n: int):
    time.sleep(1)
    for num in range(n):
        time.sleep(1)
        conn.rpush('test_list', f'message #{num}')


if __name__ == '__main__':
    run_list_queue()
