import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.draw.polygon(screen, (255, 255, 0), [[50, 100], [150, 200], [180, 210], [25, 300]])

    pygame.display.flip()