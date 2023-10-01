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
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            click_marker_x = event.x
            click_marker_y = event.y
            click_marker.append((click_marker_x, click_marker_y, False))

# 캐릭터 형상 변환 함수
def character_image(z) :
    character.clip_draw(frame * 100, z, 100, 100, x, y)

# 거리 계산 함수
def distance(x1, y1, x2, y2) :
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0

# 클릭 위치 리스트에 저장
click_marker = []
click_marker_x = x
click_marker_y = y

while running :
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # hand_arrow 표시
    for pos_x, pos_y, arrive in click_marker:
        if not arrive:
            hand_arrow.draw(pos_x, pos_y)

        character_image(100)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()