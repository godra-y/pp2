import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

pygame.mixer.music.load('bird.mp3')
pygame.mixer.music.play(-1)

clock=pygame.time.Clock()

        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)
 