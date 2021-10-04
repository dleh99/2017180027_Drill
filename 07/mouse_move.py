from pico2d import *
#import os

#os.chdir('d:/2DGP/2017180027_Drill/Lecture06_HandlingInputs')

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def Move_Charater(CharX, Chary, dmx, dmy):
    global isLeft
    global disX, disY
    if CharX > dmx:
        isLeft = True
    else:
        isLeft = False

    if CharX > dmx:
        disX = -1
    else:
        disX = 1

    if Chary > dmy:
        disY = -1
    else:
        disY = 1



def handle_events():
    global running
    global x, y
    global Chx, Chy
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x + 25, KPU_HEIGHT - 27 - event.y
            mx = event.x
            my = KPU_HEIGHT - event.y - 1
            Move_Charater(Chx, Chy, mx, my)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)


# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
isLeft = False
Chx, Chy = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
disX, disY = 0, 0
mx, my = 0, 0
frame = 0
speed = 200
# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if isLeft:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, Chx, Chy)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, Chx, Chy)
    mouse.draw(x, y)
    hide_cursor()

    Chx += disX * abs(Chx - mx) / speed
    Chy += disY * abs(Chy - my) / speed

    if Chx == mx:
        disX = 0
    if Chy == my:
        disY = 0

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




