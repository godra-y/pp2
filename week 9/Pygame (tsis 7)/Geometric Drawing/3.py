import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
            
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 10, 100, 100), 10)
    pygame.draw.circle(screen, (0, 255, 0), (300, 60), 50, 10)

    pygame.display.flip()