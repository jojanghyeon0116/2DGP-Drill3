from pico2d import *
import math

def draw_boy(x: float, y: float, boy, grass):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle(boy, grass):
    # 아래로 이동
    for x in range(400, 780, 5):
        draw_boy(x, 90, boy, grass)
    # 오른쪽으로 이동
    for y in range(90, 560, 5):
        draw_boy(780, y, boy, grass)
    # 위로 이동
    for x in range(780, 20, -5):
        draw_boy(x, 560, boy, grass)
    # 왼쪽으로 이동
    for y in range(560, 90, -5):
        draw_boy(20, y, boy, grass)
    # 아래로 복귀
    for x in range(20, 400, 5):
        draw_boy(x, 90, boy, grass)

def move_triangle(boy, grass):
    # 아래로 이동
    for x in range(400, 780, 5):
        draw_boy(x, 90, boy, grass)
    # 대각선 위로 이동 (삼각형의 오른쪽 변)
    steps = (780 - 400) // 5
    for i in range(steps + 1):
        x = 780 - i * 5
        y = 90 + i * ((345 - 90) / steps)
        draw_boy(x, y, boy, grass)
    # 대각선 아래로 이동 (삼각형의 왼쪽 변)
    for i in range(steps + 1):
        x = 400 - i * 5
        y = 345 - i * ((345 - 90) / steps)
        draw_boy(x, y, boy, grass)
    # 아래로 복귀
    for x in range(20, 400, 5):
        draw_boy(x, 90, boy, grass)

def move_circle(boy, grass):
    r = 215
    for deg in range(-90, 270):
        x = 400 - r * math.cos(math.radians(deg))
        y = 300 + r * math.sin(math.radians(deg))
        draw_boy(x, y, boy, grass)

def main():
    open_canvas()
    boy = load_image('character.png')
    grass = load_image('grass.png')
    while True:
        move_rectangle(boy, grass)
        move_triangle(boy, grass)
        move_circle(boy, grass)
    close_canvas()

if __name__ == '__main__':
    main()

