from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sonic_animation.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x
    global y
    global click_marker
    global click_marker_x
    global click_marker_y

    # ESC 탈출
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 캐릭터 형상 변환 함수
def character_image(z) :
    character.clip_draw(frame * 100, z, 100, 100, x, y)

def character_move() :
    pass

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0

while running :
    pass

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()