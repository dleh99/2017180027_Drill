from pico2d import *
import server
import collision

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        # ball들과 잔디의 충돌을 잔디가 체크함
        for ball in server.balls:
            if collision.collide(ball, self):
                ball.stop()

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        # fill here
        draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return 0, 0, 1600-1, 50
