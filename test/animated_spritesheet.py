import pygame as pg

FPS = 30

frames = ['frame1', 'frame2', 'frame3', 'frame4']

clock = pg.time.Clock()

current_frame = 0
last_update = 0

def animate():
    global last_update
    global current_frame
    now = pg.time.get_ticks()
    if now - last_update > 350:
        print(frames[current_frame])
        current_frame = (current_frame + 1) % len(frames)
        # print (now)
        last_update = now
    

while True:
    clock.tick(FPS)
    animate()
    