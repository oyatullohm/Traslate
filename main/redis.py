import redis
import json

red = redis.StrictRedis(port=6379, db=0)

class Red:
    def set(cache_key,data):
        data = json.dumps(data)
        red.set(cache_key,data)
        return True
    def get(cache_key):
        cache_data = red.get(cache_key)
        if not cache_data:
            return None
        cache_data =  cache_data.decode("utf-8")
        cache_data = json.loads(cache_data)
        return cache_data
