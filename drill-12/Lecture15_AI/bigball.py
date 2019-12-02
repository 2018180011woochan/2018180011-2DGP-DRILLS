import random
from pico2d import *
import game_world
import game_framework

class BigBall:
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0, 1000 - 1), random.randint(0, 1000 - 1)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

        # fill here for def stop

    def stop(self):
        pass