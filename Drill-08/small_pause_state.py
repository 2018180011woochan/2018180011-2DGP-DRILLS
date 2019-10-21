import game_framework
import main_state
from pico2d import *


name = "SmallPauseState"
image = None
mysec = 0

def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass



def update():

    pass


def draw():
    global mysec
    clear_canvas()
    image.draw(400, 300, 100, 100)
    main_state.draw()
    mysec = mysec + 1
    if (mysec % 2 == 1):
        image.draw(400, 300, 100, 100)
        delay(0.01)
    delay(0.01)

    update_canvas()
    pass








def pause():

    pass


def resume():
    pass


