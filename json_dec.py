import functools
import json


def to_json(get_data):
    @functools.wraps(get_data)
    def inner(*args, **kwargs):
        k = json.dumps(get_data(*args, **kwargs))
        return k
    return inner
