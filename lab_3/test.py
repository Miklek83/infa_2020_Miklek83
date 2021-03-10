import pygame
import math
import sys

pygame.init()

res_x = 1024
res_y = 768

screen = pygame.display.set_mode((res_x, res_y))
middle_x = int(res_x/2)
middle_y = int(res_y/2)

start_x = 400
start_y = 200

while True:
    # 1 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*1, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*3, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*5, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*0, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*7, start_y+25*0, 20, 20), 0)

    # 2 rad
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*0, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*1, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*2, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*3, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*4, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*5, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*6, start_y+25*1, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*7, start_y+25*1, 20, 20), 0)

    # 3 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*1, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*3, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*5, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*2, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*7, start_y+25*2, 20, 20), 0)

    # 4 rad
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*0, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*1, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*2, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*3, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*4, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*5, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*6, start_y+25*3, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*7, start_y+25*3, 20, 20), 0)

    # 5 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*1, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*3, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*5, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*4, 20, 20), 0)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(start_x+25*7, start_y+25*4, 20, 20), 0)

    # 6 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*1, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*3, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*5, start_y+25*5, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*5, 20, 20), 0)

    # 7 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*1, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*3, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*5, start_y+25*6, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*6, 20, 20), 0)
    
    # 8 rad
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*0, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*1, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*2, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*3, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*4, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*5, start_y+25*7, 20, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(start_x+25*6, start_y+25*7, 20, 20), 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    pygame.time.wait(10)
