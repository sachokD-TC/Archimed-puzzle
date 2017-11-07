from turtle import *
from model.Levels import Levels
from view.PuzzleView import PuzzleView
from model.GameElements import GameElements

START_LEVEL = 13

LIVES_NUM = 4

DOWN = 'Down'

UP = 'Up'

LEFT = 'Left'

RIGHT = 'Right'


def move(x, y, coord):
    global is_moving, ge, turtle, life
    if not is_moving and coord is not None:
        is_moving = True
        is_turned = False
        line = [[coord[0], coord[1]]]
        small_line = [[coord[0], coord[1]]]
        while (coord is not None and in_fence(x, y) and not is_black([coord[0] + x, coord[1] + y])):
            coord[0] += x
            coord[1] += y
            line.append([coord[0], coord[1]])
            small_line.append([coord[0], coord[1]])
            if y == 0 and x == 1: v.go_right(turtle)
            if x == -1 and y == 0: v.go_left(turtle)
            if x == 0 and y == 1: v.go_up(turtle)
            if y == -1 and x == 0: v.go_down(turtle)
            is_turned = True
            ge.add_to_complited(coord)
            v.set_brick_to_complited(ge.get_brick(coord[0], coord[1]))
            if len(small_line) == 2:
                if ge.is_small_line_in_lines(small_line) and not ge.is_level_complete(
                        levels.levels[lev].get_number_of_complete_bricks()):
                    next_level(0)
                    coord = None
                    line = None
                else:
                    small_line = []
        if ge.is_level_complete(levels.levels[lev].get_number_of_complete_bricks()):
            next_level(1)
            coord = None
            line = None
        if coord is not None and ge.is_passed([coord[0], coord[1]]) and is_turned and not ge.is_level_complete(
                levels.levels[lev].get_number_of_complete_bricks()):
            next_level(0)
        else:
            if line is not None and coord is not None:
                ge.add_to_passed(coord)
                is_moving = False
                ge.add_to_lines(line)


def is_black(point):
    return point in levels.levels[lev].black_bricks


def in_fence(x, y):
    if coord[0] + x > levels.levels[lev].sizex - 1 or coord[0] + x < 0:
        return False
    if coord[1] + y > levels.levels[lev].sizey - 1 or coord[1] + y < 0:
        return False
    return True


def right():
    global coord
    move(1, 0, coord)


def left():
    global coord
    move(-1, 0, coord)


def up():
    global coord
    move(0, 1, coord)


def down():
    global coord
    move(0, -1, coord)


def click_on_menu_item(x, y):
    global start_click, rules_click, about_click
    if x > -100 and x < 300 and y > -50 and y < 100:
        if start_click == 1:
            next_level(0)
        else:
            v.highlight_start()
            start_click += 1
    if x > -100 and x < 300 and y > -150 and y < -100:
        start_click = 0
        v.highlight_rules()
    if x > -100 and x < 300 and y > -250 and y < -160:
        start_click = 0
        v.highlight_about()


def next_level(inc):
    global sc, lev, is_moving, turn, coord, ge, turtle, life
    if inc == 0:
        life -= 1
        if life <= 0:
            start_from_begining()
            return
    v.set_window(sc)
    ge.clean_passed()
    ge.clean_complited()
    ge.clean_lines()
    lev += inc
    is_moving = False
    turn = None
    coord = levels.levels[lev].start_point[:]
    ge.add_to_complited(coord)
    ge.setup_bricks_array(levels.levels[lev].sizex, levels.levels[lev].sizey)
    v.draw_level(levels.levels[lev], ge, lev, life)
    start = levels.levels[lev].start_point
    turtle = v.goto_start(start, ge.get_brick(start[0], start[1]))
    sc.onkey(up, 'Up')
    sc.onkey(down, 'Down')
    sc.onkey(right, 'Right')
    sc.onkey(left, 'Left')
    sc.listen()


def start_from_begining():
    global v, sc, life
    life = LIVES_NUM
    v.set_window(sc)
    v.draw_menu(sc)
    sc.onscreenclick(click_on_menu_item)
    sc.mainloop()


start_click = 0
rules_click = 0
about_click = 0
life = LIVES_NUM
levels = Levels()
turtle = getturtle()
sc = Screen()
v = PuzzleView()
ge = GameElements()
v.set_window(sc)
lev = START_LEVEL
is_moving = False
turn = None
ge.register_bricks()
ge.register_level_numbers()
start_from_begining()
