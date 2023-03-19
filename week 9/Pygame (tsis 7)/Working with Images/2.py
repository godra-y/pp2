import pygame
pygame.init()

screen=pygame.display.set_mode((400, 300))

clock=pygame.time.Clock()

ball_surf=pygame.image.load('ball.png')
screen.fill((255, 255, 255))
screen.blit(ball_surf, (20, 20))
        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)