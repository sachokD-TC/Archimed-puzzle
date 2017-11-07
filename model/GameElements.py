from turtle import *
import os


class GameElements:
    GIF_EXTENSION = ".gif"
    PIC_FOLDER = 'resources/pic/'
    bricks = None
    brick_names = ['white', 'black', 'target', 'white_on', 'title_box', 'menu_box', 'start_rollover', 'rules_rollover',
                   'credits_rollover', 'level_box']
    passed_bricks = []
    lines_passed = []
    complited_bricks = []

    def __init__(self):
        print('')

    def setup_bricks_array(self, w, h):
        self.bricks = [[None for x in range(w)] for y in range(h)]

    def add_to_bricks(self, x, y, turtle):
        self.bricks[x][y] = turtle

    def get_brick(self, x, y):
        return self.bricks[x][y]

    def add_to_lines(self, line):
        self.lines_passed.append(line)

    def add_to_passed(self, point):
        self.passed_bricks.append([point[0], point[1]])

    def add_to_complited(self, point):
        if point not in self.complited_bricks:
            self.complited_bricks.append([point[0], point[1]])

    def is_level_complete(self, number_to_compare):
        return (len(self.complited_bricks) - number_to_compare) >= 0

    def is_small_line_in_lines(self, small_line):
        for i in self.lines_passed:
            if small_line[0] in i and small_line[1] in i:
                return True
        return False

    def is_passed(self, point):
        return point in self.passed_bricks

    def clean_passed(self):
        self.passed_bricks = []

    def clean_complited(self):
        self.complited_bricks = []

    def clean_lines(self):
        self.lines_passed = []

    def register_bricks(self):
        for s in GameElements.brick_names:
            register_shape(GameElements.PIC_FOLDER + s + GameElements.GIF_EXTENSION)

    def register_level_numbers(self):
        for i in range(0,10):
            register_shape(GameElements.PIC_FOLDER + str(i) + GameElements.GIF_EXTENSION)
