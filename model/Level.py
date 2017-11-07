class Level:
    def __init__(self, name, size, black_bricks, levels=None):
        self.name = name
        self.sizex = size[0]
        self.sizey = size[1]
        self.black_bricks = black_bricks
        self.black_bricks.sort()
        self.start_point = levels[0].start
        self.levels = levels

    def get_number_of_complete_bricks(self):
        return self.sizey * self.sizex - len(self.black_bricks)
