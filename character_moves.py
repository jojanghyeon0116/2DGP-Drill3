from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def move_top():
    print('Moving top')
    for x in range(780, 20, -5):
        draw_boy(x, 560)
    pass


def move_right():
    print('Moving right')
    for y in range(90, 560, 5):
        draw_boy(780, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(400, 780, 5):
        draw_boy(x, 90)
    pass


def move_left():
    print('Moving left')
    for y in range(560, 90, -5):
        draw_boy(20, y)
    pass


def move_bottom_return():
    print('Moving bottom return')
    for x in range(20, 400, 5):
        draw_boy(x, 90)
    pass

def move_rectangle():
    print("MOVE RECTANGLE")
    move_bottom()
    move_right()
    move_top()
    move_left()
    move_bottom_return()
    pass


def move_circle():
    print("MOVE CIRCLE")
    r = 235
    for deg in range(-90, 270):
        x = 400 - r * math.cos(math.radians(deg))
        y = 325 + r * math.sin(math.radians(deg))
        draw_boy(x, y)
    pass

def move_crossline_up():
    print("MOVE CROSSLINE UP")
    steps = 380 // 5
    for i in range(steps + 1):
        x = 780 - i * 5
        y = 90 + i * 6.2
        draw_boy(x, y)
    pass


def move_crossline_down():
    print("MOVE CROSSLINE DOWN")
    steps = 380 // 5
    for i in range(steps + 1):
        x = 380 - i * 5
        y = 560 - i * 6.2
        draw_boy(x, y)
    pass


def move_triangle():
    print("MOVE TRIANGLE")
    move_bottom()
    move_crossline_up()
    move_crossline_down()
    move_bottom_return()
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

while True:
    move_rectangle()
    move_triangle()
    move_circle()
    pass

close_canvas()
