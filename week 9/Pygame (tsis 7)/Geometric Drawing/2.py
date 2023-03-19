import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.draw.circle(screen, (0, 128, 255), (200, 150), 50)

    pygame.display.flip()