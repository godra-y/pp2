import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.draw.lines(screen, (255, 255, 0), True, [(200, 80), (250, 80), (300, 20)], 3)

    pygame.display.flip()