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
    
    rot = (255,0,0)
    blau = (0,0,255)
    #zeichne einen Kreis mit (Screen, Farbe, Kreismittelpunkt, Radius)
    pygame.draw.circle(screen, blau, (250,250), 75)
    #zeichne ein Rechteck mit (Screen, Farbe, (left, top, breite, hoehe))
    pygame.draw.rect(screen, rot, (10,10,50,50))
    #weitere Zeichenfunktionen: https://www.pygame.org/docs/ref/draw.html#pygame.draw
    
    #erneuere die Anzeige auf dem Bildschirm (lade Buffer)
    pygame.display.flip()

pygame.quit()
