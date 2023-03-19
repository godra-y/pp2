import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

is_blue=True

while True:
    if is_blue: color=(0, 128, 255)
    else: color=(255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_blue=not is_blue
        if event.type==pygame.QUIT:
            exit()

    pygame.display.flip()