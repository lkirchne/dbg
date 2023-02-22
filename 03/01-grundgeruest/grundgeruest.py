import pygame
pygame.init()

# Setze die Auflösung auf 500x500 Pixel
screensize = (500,500)
screen = pygame.display.set_mode(screensize)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Button (x) wurde gedrueckt
            running = False
    
    #setze die Hintergrundfarbe auf (255,255,255) = (R,G,B) = weiss
    screen.fill((255,255,255))
    
    #male einen Kreis mit (Screen, Farbe, Kreismittelpunkt, Radius)
    #beispiele: https://www.pygame.org/docs/ref/draw.html#pygame.draw
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)
    pygame.draw.rect(screen, (255,0,0),(10,10,50,50), 50)
    
    #erneuere die Anzeige auf dem Bildschirm (lade Buffer)
    pygame.display.flip()

pygame.quit()
