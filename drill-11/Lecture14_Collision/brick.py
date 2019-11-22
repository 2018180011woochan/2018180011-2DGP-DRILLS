from pico2d import *

class Brick:
    def __init__(self):
        self.x, self.y, self.value = 800, 100, 1
        self.image = load_image('brick180x40.png')

    def update(self):
        self.x += self.value

        if self.x > 1400:
            self.value *= -1
        elif self.x < 200:
            self.value *= -1

    def draw(self):
        self.image.draw(self.x, self.y)

    # fill here
    def get_bb(self):
        return self.x - 50, self.y + 20, self.x + 50, self.y + 20