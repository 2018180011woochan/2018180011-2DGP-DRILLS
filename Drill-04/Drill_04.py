from pico2d import *


def handle_events():
    global running
    global p
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                p = False
            elif event.key == SDLK_LEFT:
                dir -= 1
                p = False


            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                p = False
            elif event.key == SDLK_LEFT:
                dir += 1
                p = True


    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
p = False

x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    if (dir == 0):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, 90)
    elif (dir < 0):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)

    if (p == True):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, 90)

    if (x > 800):
        x -= 10
    elif (x < 0):
        x += 10


    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir


    #delay(0.01)



close_canvas()

