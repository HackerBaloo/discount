from nameko.rpc import rpc
from nameko_redis import Redis

class Storage:
    name = "storage"
    database = Redis()

    @rpc
    def store(self, key, data):
        self.redis.set(key, data)
        print(f'saved: {data} at: {key}')

    @rpc
    def get(self, key):
        data = self.redis.get(key)
        print(f'got: {data} at: {key}')
        return data

