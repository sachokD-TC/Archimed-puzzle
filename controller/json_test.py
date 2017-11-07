import json

level_json = '{"name": "Test", "size": [6, 6], "walls": [[0, 0], [0, 3], [2, 3], [2, 5], [3, 2], [5, 0]]}'


class Level(object):
    def __init__(self, name, size, walls):
        self.name = name
        self.size = size
        self.walls = walls



def jsonTest():
   level = json.loads(level_json, lambda d: Namespace(**d))
   print(level)


try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

jsonTest()