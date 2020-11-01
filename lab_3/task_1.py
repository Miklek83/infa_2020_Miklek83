import pygame
from pygame.draw import *

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255,255,0)
LIGHTGRAY = (200,200,200)
GRAY = (100,100,100)
FPS = 30

screen = pygame.display.set_mode((400, 400))

rect(screen,LIGHTGRAY,(0,0,400,400))
circle(screen, BLACK, (200, 200), 100, 1)
circle(screen, YELLOW, (200, 200), 99, 0)
# Левый глаз
circle(screen, BLACK, (160, 170), 23, 1)
circle(screen, RED, (160, 170), 22, 0)
circle(screen, BLACK, (160, 170), 8, 0)
line(screen, BLACK, (100,120), (175,135), 15)


# Правый глаз
circle(screen, BLACK, (240, 170), 18, 1)
circle(screen, RED, (240, 170), 17, 0)
circle(screen, BLACK, (240, 170), 8, 0)


pygame.draw.rect (screen, (0,0,0),[15,300,20,200])
pygame.draw.rect (screen, (0,0,0),[50,350,40,150])
pygame.draw.rect (screen, (0,0,0),[120,290,30,210])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
