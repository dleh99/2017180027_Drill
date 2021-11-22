import random

from pico2d import *

import game_framework
import game_world
import server
import collision


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200 # 200 pixel per second
        self.child_balls = []

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x > 1600:
            self.x = 1600
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed

        for ball in server.balls.copy():
            if collision.collide(ball, self):
                self.attach_ball(ball)
                server.balls.remove(ball)
            else:
                for c_ball in self.child_balls:
                    if collision.collide(ball, c_ball):
                        self.attach_ball(ball)
                        server.balls.remove(ball)
                        break

        if len(self.child_balls) >= 10:
            for ball in self.child_balls:
                ball.set_parent(None)
                server.balls.append(ball)
                game_world.remove_object(server.brick)


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def attach_ball(self, ball):
        self.child_balls.append(ball)
        ball.set_parent(self) # 볼에 대해서 부모를 정한다.

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

