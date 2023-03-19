import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

while True:
    pygame.draw.rect(screen, (0,  128,  255 ), pygame.Rect(30,  30,  60,  60))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    pygame.display.flip()
