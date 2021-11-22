import random
from pico2d import *
import game_world
import game_framework


class Ball:
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 400 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 600, random.randint(Ball.MIN_FALL_SPEED, Ball.MAX_FALL_SPEED)
        self.move_speed = 0
        self.parent = None
        self.rx, self.ry = 0, 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.parent is None: # 볼에 부모가 없음
            self.y -= self.fall_speed * game_framework.frame_time
        else:
            self.x, self.y = self.parent.x + self.rx, self.parent.y + self.ry

    def set_parent(self, brick):
        self.parent = brick
        if brick is not None:
            self.rx, self.ry = self.x - brick.x, self.y - brick.y
        else:
            self.rx, self.ry = 0, 0

    def stop(self):
        self.fall_speed = 0


