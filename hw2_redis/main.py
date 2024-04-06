import redis
import time
import json


def data_string_test(file_name: str, client: redis.Redis):

    time_start = time.time()

    with open(file_name) as f:
        client.set("data_string", f.read())

    time_save = time.time()

    client.get("data_string")

    time_end = time.time()

    print("STRING")
    print("Load time: ", time_save - time_start)
    print("Get time: ", time_end - time_save)
    print()


def data_zset_test(file_name: str, client: redis.Redis):

    with open(file_name) as f:
        data = dict([(str(el), i) for i, el in enumerate(json.loads(f.read()))])

    time_start = time.time()

    client.zadd("data_zset", mapping=data)

    time_save = time.time()

    client.zrange("data_zset", 0, -1)

    time_end = time.time()

    print("ZSET")
    print("Load time: ", time_save - time_start)
    print("Get time: ", time_end - time_save)
    print()


def data_hset_test(file_name: str, client: redis.Redis):

    with open(file_name) as f:
        data = dict([(i, str(el)) for i, el in enumerate(json.loads(f.read()))])

    time_start = time.time()

    client.hset("data_hset", mapping=data)

    time_save = time.time()

    client.hgetall("data_hset")

    time_end = time.time()

    print("HSET")
    print("Load time: ", time_save - time_start)
    print("Get time: ", time_end - time_save)
    print()


def data_list_test(file_name: str, client: redis.Redis):
    with open(file_name) as f:
        data = [str(el) for el in json.loads(f.read())]

    time_start = time.time()

    client.lpush("data_list", *data)

    time_save = time.time()

    client.lrange("data_list", 0, -1)

    time_end = time.time()

    print("LIST")
    print("Load time: ", time_save - time_start)
    print("Get time: ", time_end - time_save)
    print()


def main():
    file = "data.json"
    client = redis.Redis(host='localhost', port=6379, db=0)
    data_string_test(file, client)
    data_zset_test(file, client)
    data_hset_test(file, client)
    data_list_test(file, client)


if __name__ == "__main__":
    main()
redis-server /usr/local/etc/redis/redis.conf