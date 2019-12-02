import random
from pico2d import *
import game_world
import game_framework
import background

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, background.get_canvas_width()), random.randint(0, background.get_canvas_height())



    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    #fill here for def stop
    def stop(self):
        pass

    def do(self):
        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(0, self.y, self.bg.h)


# fill here
# class BigBall
