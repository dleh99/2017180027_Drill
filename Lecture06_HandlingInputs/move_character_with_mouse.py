from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def Move_Charater(CharX, Chary, mx, my):
    pass

def handle_events():
    global running
    global x, y
    global isLeft
    global Chx, Chy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x + 25, KPU_HEIGHT - 27 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Chx, Chy = event.x, KPU_HEIGHT - event.y - 1
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                isLeft = True
            elif event.key == SDLK_RIGHT:
                isLeft = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)


# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
isLeft = False
Chx, Chy = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
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

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




