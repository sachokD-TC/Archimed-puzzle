import json
from model.Level import Level


class LevelsInfo():
    def __init__(self, id, start, complexity, minLength, maxLength):
        self.id = id
        self.start = start
        self.complexity = complexity
        self.minLength = minLength
        self.maxLength = maxLength


class Deserializer():
    def as_level(self, dct):
        if 'name' in dct:
            return Level(dct['name'], dct["size"], dct["walls"], dct['levels'])
        else:
            return LevelsInfo(dct["id"], dct['start'], dct['complexity'], dct['minLength'], dct['maxLength'])

    def deserialize(self, csruct):
        return json.loads(csruct, object_hook=self.as_level)
