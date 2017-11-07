from model.JSONLevels import JSONLevels
from model.Deserializer import Deserializer


class Levels():
    levels = []

    def __init__(self):
        des = Deserializer()
        JSONLevels().load_levels_from_file('resources/levels/levels.json')
        for i in JSONLevels().cstruct:
            self.levels.append(des.deserialize(i))

            # self.levels = [
            #     Level(3, 3, [1, 1], [[0, 0]]),
            #     Level(4, 4, [0, 1], [[0, 0], [3, 0], [3, 1]]),
            #     Level(4, 4, [1, 3], [[0, 0], [0, 3], [3, 0]]),
            #     Level(4, 4, [0, 2], [[2, 2], [3, 0]]),
            #     Level(4, 4, [1, 1], [[0, 2], [0, 3], [3, 0]]),
            #     Level(5, 5, [2, 1], [[1, 1], [1, 2], [1, 3], [4, 1]]),
            #     Level(5, 5, [1, 2], [[0, 2], [3, 1], [4, 4]]),
            #     Level(5, 5, [2, 4], [[0, 4], [1, 1], [2, 0], [4, 4]]),
            #     Level(5, 5, [0, 1], [[0,4], [1, 2], [1, 4], [3, 0],[3,2],[4,0]]),
            #     Level(6, 6, [3, 1], [[0, 0], [0, 5], [2, 2], [3, 3], [3, 5], [5, 3]]),
            #     Level(8, 8, [3, 6], [[0, 3], [3, 7], [5, 4], [5, 6], [6, 6], [7, 2]])
            # ]
