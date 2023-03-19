import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.draw.rect(screen, (123, 45, 145), pygame.Rect(60, 60, 80, 80))

    pygame.display.flip()