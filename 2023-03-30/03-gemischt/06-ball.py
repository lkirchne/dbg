# User Story: Das Programm bewegt einen Ball in der Diagonale über den Bildschirm. Der Ball soll an den Fensterrändern abprallen. Mit den Pfeiltasten links und rechts kann man die Richtung des Ball beeinflussen.
# maximale Anzahl Fehler: 3
import sys, pygame, os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # wechsel in den Ordner, wo die .py Datei liegt

pygame.init()
size = width, height = 640, 480
bg = 205, 205, 205
speed = [2,2]

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()

while True:
    pygame.time.Clock().tick(60) # begrenzt die Schleife auf 60 Aufrufe pro Sekunde (max. 60 FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -2
            if event.key == pygame.K_RIGHT:
                speed[0] = 2
            if event.key == pygame.K_UP:
                height -= 10
    
    if ballrect.left < 0 or ballrect.right > height:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 400:
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed) # bewege das Rechteck ballrect

    screen.fill(bg)
    screen.blit(ball, ballrect) # bewege den Ball zur Position des Rechtecks ballrect
    pygame.display.flip()
