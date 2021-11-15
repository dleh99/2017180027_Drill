import game_framework
from pico2d import *
import random

import game_world

# Bird Run Speed
PIXEL_PER_Cent = (100.0 / 20)
PIXEL_PER_METER = (100.0 / 0.2)  # 100 pixel 20 cm < 참새 평균 신장
RUN_SPEED_KMPH = 20.0  # Km / Hour = 참새 속력 시속 20~40km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 1 / 60        # 참새는 아니고, 벌새의 경우 초당 60번의 날개짓을 한다 함.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14



# Bird Event
GO_RIGHT, GO_LEFT = range(2)


# Bird States

key_event_table = {

}

class RightState:

    def enter(bird, event):
        pass

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        if bird.x >= 1600 - 20:
            bird.add_event(GO_LEFT)

    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 20, 20)        # 참새 평균 신장 20cm


class LeftState:

    def enter(bird, event):
        pass

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x -= bird.velocity * game_framework.frame_time
        if bird.x <= 0 + 20:
            bird.add_event(GO_RIGHT)

    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y, 20, 20)


next_state_table = {
    RightState: {GO_RIGHT: RightState, GO_LEFT: LeftState},
    LeftState: {GO_RIGHT: RightState, GO_LEFT: LeftState}
}

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(50, 300), random.randint(90, 600)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.event_que = []
        self.cur_state = RightState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

