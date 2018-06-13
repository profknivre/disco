__version__ = '0.2.0'
from xmlrpc.client import ServerProxy


class DiscoServer:
    def __init__(self, redis_url='redis://localhost'):
        import redis

        self.r = redis.StrictRedis.from_url(redis_url)
        self.prefix = 'disco_'

    def announce(self, name, path):
        print('Announcing {:s} => "{:s}"'.format(name, path))
        self.r.set('{:s}{:s}'.format(self.prefix, name), path)

    def discover(self, name):
        ret = self.r.get('{:s}{:s}'.format(self.prefix, name))
        if ret is None:
            return None
        return ret.decode('ascii')

    def denounce(self, name):
        print('Denouncing {:s}'.format(name))
        self.r.delete('{:s}{:s}'.format(self.prefix, name))


class DiscoClient:
    def __init__(self, server_url=None):
        if server_url is None:
            import os
            server_url = os.environ.get('DISCO_SEVER',
                                        'http://44.0.0.181:8888')

        self.s = ServerProxy(server_url, allow_none=True)

    def __getattr__(self, item):
        return getattr(self.s, item)


class DiscoProxy(DiscoClient):
    def __init__(self, service, server_url=None):
        super().__init__(server_url)
        url = self.s.discover(service)
        self.s = ServerProxy(url, allow_none=True)


class DiscoProxy2(DiscoClient):
    def __getattr__(self, item):
        url = self.s.discover(item)
        return ServerProxy(url, allow_none=True)
