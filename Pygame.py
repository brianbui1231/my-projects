import pygame
from sys import exit
import random
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
title = pygame.display.set_caption("Stick Game")
bg = pygame.Surface((200, 100))
bg.fill("Red")
text = pygame.font.Font(None, 50)
score = 0
ts = text.render(f"Score: {score}", False, "Blue")
def stickMan(screen, x, y):
    pygame.draw.ellipse(screen, 'White', [0+x, 0+y, 10, 10], 0)
    pygame.draw.line(screen, "White", [4 +x, 17+y], [4+x, 7 + y], 2)
    pygame.draw.line(screen,'White',[4+x,17+y],[9+x,27+y], 2)
    pygame.draw.line(screen,'White',[4+x,17+y],[-1+x,27+y], 2)
    pygame.draw.line(screen,'White',[4+x,7+y],[8+x,17+y], 2)
    pygame.draw.line(screen,'White',[4+x,7+y],[0+x,17+y], 2)
def object1(screen, x, y):
    pygame.draw.rect(screen, 'White', (15+x, 15+y, 15, 15))
pygame.mouse.set_visible(1)
xC = 8
yC = 470
xS = 0
yS = 0
xO = 400
yO = 470
objectSpeed = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xS = -1
            if event.key == pygame.K_RIGHT:
                xS = 1
            if event.key == pygame.K_UP:
                yS = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xS = 0
            if event.key == pygame.K_RIGHT:
                xS = 0
            if event.key == pygame.K_UP:
                yS = 1
    if xC >= 780:
        xS = 0
        xC -= 1
    elif xC <= 8:
        xS = 0
        xC += 1
    elif yC > 470:
        yS = 0
        yC -= 1
    elif yC <= 450:
        yS = 0
        yC += 1
    else:
        yC += yS
        xC += xS
    xO -= objectSpeed
    score += 1
    if xO <= -20:
        xO = 740
    if (xO <= xC and yC > yO):
        if xO <= xC and yC == yO:
            xO = 740
            score -= score
            objectSpeed == objectSpeed
    else    
    if score % 1000 == 0:
        objectSpeed += 0.5
    pygame.display.update()
    ts = text.render(f"Score: {score}", True, "Blue")
    screen.fill((0, 0, 0))
    screen.blit(ts, (350, 50))
    clock.tick(60)
    stickMan(screen, xC, yC)
    object1(screen, xO, yO)

    print(f'stick: {xC}, {yC}')
    print(f'object: {xO}, {yO}')