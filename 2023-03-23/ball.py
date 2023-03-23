import sys, pygame
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
size = width, height = 640, 480
speed = [2, 2]
bg = 205, 205, 205
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()

while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(ball, ballrect)
    pygame.display.flip()