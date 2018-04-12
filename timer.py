import pygame as pg

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
font = pg.font.Font(None, 54)
font_color = pg.Color('springgreen')

passed_time = 0
timer_started = False
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    start_time = pg.time.get_ticks()

    if timer_started:
        passed_time = pg.time.get_ticks() - start_time

    screen.fill((30, 30, 30))
    text = font.render(str(passed_time/1000), True, font_color)
    screen.blit(text, (50, 50))

    pg.display.flip()
    clock.tick(30)

pg.quit()