from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 8)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8


class Small_Ball:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(5, 20)
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.clip_draw(0, 0, 23, 23, self.x, self.y)

    def update(self):
        if self.y > 70:
            self.y -= self.speed


class Big_Ball:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(5, 20)
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.clip_draw(0, 0, 43, 43, self.x, self.y)

    def update(self):
        if self.y > 80:
            self.y -= self.speed

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

num = random.randint(1, 20)

grass = Grass()
team = [Boy() for i in range(1, 11 + 1)]
Small_Balls = [Small_Ball() for i in range(1, num)]
Big_Balls = [Big_Ball() for i in range(num, 20 +1)]

running = True

# game main loop code
while running:
    handle_events()

    #game logic
    for boy in team:
        boy.update()
    for Small in Small_Balls:
        Small.update()
    for Big in Big_Balls:
        Big.update()
    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for Small in Small_Balls:
        Small.draw()
    for Big in Big_Balls:
        Big.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()