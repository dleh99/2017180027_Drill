from pico2d import *
import game_framework
import main_state

name = 'pause_state'
image = None
blink_time = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def update():
    global blink_time
    blink_time += 0.01
    if blink_time > 2:
        blink_time = 0

def draw():
    global image, blink_time
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if blink_time < 1:
        image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                if main_state.ispause:
                    main_state.ispause = False
                    game_framework.pop_state()