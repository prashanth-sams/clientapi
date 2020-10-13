from .client import ClientApi


def request(method, url, **kwargs):
    return ClientApi().request(method=method, url=url, **kwargs)


def get(url, headers=None, body=None):
    if headers is None: headers = {}
    return request('get', url, headers=headers, body=body)


def post(url, headers=None, body=None):
    if headers is None: headers = {}
    return request('get', url, headers=headers, body=body)


def put(url, headers=None, body=None):
    if headers is None: headers = {}
    return request('get', url, headers=headers, body=body)


def patch(url, headers=None, body=None):
    if headers is None: headers = {}
    return request('get', url, headers=headers, body=body)


def delete(url, headers=None, body=None):
    if headers is None: headers = {}
    return request('get', url, headers=headers, body=body)
