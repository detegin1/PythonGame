import pygame
import random
pygame.init()
win = pygame.display.set_mode((1000, 1000))

def labirint():
    pygame.draw.line(win, 'black', (50, 50), (50, 300), 5)
    pygame.draw.line(win, 'black', (50, 300), (300, 300), 5)
    pygame.draw.line(win, 'black', (300, 300), (300, 90), 5)
    pygame.draw.line(win, 'black', (50, 300), (300, 300), 5)

x = 500
y = 500

z = 700
c = 700

win.fill((100,0,100))
pygame.draw.circle(win, 'green', (x, y), 50)
pygame.draw.rect(win, 'red', (z,c, 50,50))
labirint()
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_a]:
        x -= 3
        y -= 3
        z-=random.randint(0,10)
        c-=random.randint(0,10)
    if keys[pygame.K_w] and keys[pygame.K_d]:
        x += 3
        y -= 3
    if keys[pygame.K_a] and keys[pygame.K_s]:
        x -= 3
        y += 3
    if keys[pygame.K_s] and keys[pygame.K_d]:
        x += 3
        y += 3

    elif keys[pygame.K_a]:
        x -=3
    elif keys[pygame.K_d]:
        x +=3
    elif keys[pygame.K_w]:
        y -=3
    elif keys[pygame.K_s]:
        y +=3

    if y <0:
        y=10
    if y >1000:
        y=990
    if x>1000:
        x=990
    if x<0:
        x=10
    if z < 0:
        z = 10
    if z > 1000:
        z = 990
    if c > 1000:
        c = 990
    if c < 0:
        c = 10


    win.fill((100, 0, 100))
    pygame.draw.circle(win, 'green', (x, y), 30)
    pygame.draw.rect(win, 'red', (z, c, 50, 50))
    labirint()
    pygame.display.update()
    pygame.time.delay(10)




