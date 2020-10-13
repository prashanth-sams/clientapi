import urllib3


class ClientApi(object):
    __attrs__ = [
        'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
        'cert', 'adapters', 'stream', 'trust_env',
        'max_redirects',
    ]

    def __init__(self):
        self.http = urllib3.PoolManager()

    def request(self, method, url, **kwargs):
        return self.http.request(method.upper(), url)