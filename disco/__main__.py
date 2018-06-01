if __name__ == '__main__':
    from xmlrpc.server import DocXMLRPCServer
    import os
    from disco import DiscoServer

    redis_url = os.environ.get('REDIS_URL','redis://localhost')

    instance = DiscoServer(redis_url)

    with DocXMLRPCServer(('', 8888),allow_none=True) as server:
        server.register_instance(instance)
        server.serve_forever()
