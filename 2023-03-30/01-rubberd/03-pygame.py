# User Story: Es soll ein Quadrat in der Farbe rot und dann grün abwechselnd blinken
# maximale anzahl Fehler: 2
import sys, pygame, os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # wechsel in den Ordner, wo die .py Datei liegt

pygame.init()
size = width, height = 240, 240
colorBackground = 205, 205, 205
red = 255, 0, 0
green = 255, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    screen.fill(colorBackground)
    pygame.draw.rect(screen, red, (100,100,50,50))
    pygame.display.flip()

    pygame.time.delay(1000) # warte 1 Sekunde

    pygame.draw.rect(screen, green, (100,100,50,50))
    screen.fill(colorBackground)
    pygame.display.flip()

    pygame.time.delay(1000) # warte 1 Sekunde
