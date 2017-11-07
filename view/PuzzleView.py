from turtle import *
import math
from model.GameElements import GameElements
from model.Level import Level

LIVES_Y = -300

LIVES_X = 300

TITLE_Y = 250

START_Y = 0

START_X = 0

TARGET = GameElements.PIC_FOLDER + 'target' + GameElements.GIF_EXTENSION
WHITE_BRICK = GameElements.PIC_FOLDER + 'white' + GameElements.GIF_EXTENSION
WHITE_BRICK_ON = GameElements.PIC_FOLDER + 'white_on' + GameElements.GIF_EXTENSION
BLACK_BRICK = GameElements.PIC_FOLDER + 'black' + GameElements.GIF_EXTENSION
BG_PIC = GameElements.PIC_FOLDER + 'new_bg' + GameElements.GIF_EXTENSION
MENU_BOX = GameElements.PIC_FOLDER + 'menu_box' + GameElements.GIF_EXTENSION
TITLE_BOX = GameElements.PIC_FOLDER + 'title_box' + GameElements.GIF_EXTENSION
START_MENU = GameElements.PIC_FOLDER + 'start_rollover' + GameElements.GIF_EXTENSION
RULES_MENU = GameElements.PIC_FOLDER + 'rules_rollover' + GameElements.GIF_EXTENSION
CREDITS_MENU = GameElements.PIC_FOLDER + 'credits_rollover' + GameElements.GIF_EXTENSION
LEVEL_BOX = GameElements.PIC_FOLDER + 'level_box' + GameElements.GIF_EXTENSION
NUMBER = GameElements.PIC_FOLDER + '_num_' + GameElements.GIF_EXTENSION

class PuzzleView:
    WINDOW_TITLE = 'Archimed puzzle game'


    @staticmethod
    def set_window(sc):
        title(PuzzleView.WINDOW_TITLE)
        setup(width=1280, height=749)
        sc.clearscreen()
        sc.bgcolor('green')
        sc.bgpic(BG_PIC)

    def draw_level(self, level, ge, num, life):
        self.set_start_point(level.sizex)
        self.draw_life(life)
        penup()
        goto(-20, TITLE_Y)
        shape(LEVEL_BOX)
        clone()
        goto(80, TITLE_Y)
        if num < 10:
            shape(NUMBER.replace('_num_', str(num)))
            clone()
        else:
            shape(NUMBER.replace('_num_', str(int(num/10))))
            clone()
            goto(110, TITLE_Y)
            shape(NUMBER.replace('_num_', str(num - int(num/10)*10)))
            clone()
        m = 0
        black_bricks = level.black_bricks
        for i in range(level.sizex):
            for n in range(level.sizey):
                shape(WHITE_BRICK)
                if i == black_bricks[m][0] and n == black_bricks[m][1]:
                    shape(BLACK_BRICK)
                    if m != len(black_bricks) - 1:
                        m += 1
                goto(self.START_X + i * 50, self.START_Y + n * 50)
                ge.add_to_bricks(i, n, clone())

    def draw_life(self, life):
        penup()
        goto(LIVES_X, LIVES_Y)
        for i in range(0,life):
            shape(TARGET)
            clone()
            goto(LIVES_X+50*(i+1), LIVES_Y)

    def goto_start(self, start_point, brick):
        ht()
        color('red')
        goto(start_point[0] * 50 + self.START_X, start_point[1] * 50 + self.START_Y)
        pensize(2)
        shape(TARGET)
        st()
        brick.shape(WHITE_BRICK_ON)
        pendown()
        return PuzzleView.to_front(getturtle())

    @staticmethod
    def to_front(turtle):
        clone = turtle.clone()
        turtle.ht()
        return clone

    def draw_menu(self, sc):
        global start, rules, about
        penup()
        shape(TITLE_BOX)
        goto(0, TITLE_Y)
        clone()
        shape(MENU_BOX)
        goto(0, -100)
        clone()
        shape(START_MENU)
        ht()
        goto(0, 10)
        start = clone()
        shape(RULES_MENU)
        goto(0, -105)
        rules = clone()
        shape(CREDITS_MENU)
        goto(0, -220)
        about = clone()

    def highlight_start(self):
        global start, rules, about
        start.st()
        rules.ht()
        about.ht()

    def highlight_rules(self):
        global start, rules, about
        start.ht()
        rules.st()
        about.ht()

    def highlight_about(self):
        global start, rules, about
        start.ht()
        rules.ht()
        about.st()


    def set_start_point(self, size):
        self.START_X = -math.sqrt(2) * size * 50 / 3
        self.START_Y = self.START_X

    def set_brick_to_complited(self, turtle):
        turtle.shape(WHITE_BRICK_ON)

    def go_up(self, turtle):
        turtle.setheading(90)
        turtle.forward(50)

    def go_left(self, turtle):
        turtle.setheading(-180)
        turtle.forward(50)

    def go_right(self, turtle):
        turtle.setheading(0)
        turtle.forward(50)

    def go_down(self, turtle):
        turtle.setheading(-90)
        turtle.forward(50)
