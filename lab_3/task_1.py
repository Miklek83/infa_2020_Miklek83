import pygame
from pygame.draw import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255,255,0)
LIGHTGRAY = (200,200,200)
GRAY = (100,100,100)
FPS = 30


def main ():
    
    #Задаем размеры и координаты смайлика
    x,y=200,200
    width_smile,height_smile=350,350
    
    
    draw_smile (x,y,width_smile,height_smile)

    pygame.display.update()
    
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()
    

def draw_smile (x,y,width,height):
    '''Рисует  смайлик c центром в точке (x,y)со следующими параметрами
    x-координата центра смайлика по оси x
    y-координата центра смайлика по оси y
    width - ширина  смайлика
    height - высота смайлика
    '''

    draw_face (x,y,width,height)
    
    draw_eyes (x,y,width,height)  


def draw_face (x,y,width,height):

    circle(screen, BLACK, (x, y), width/2, 1)
    circle(screen, YELLOW, (x, y), width/2-1, 0)   
    
def draw_eyes(x,y,width,height):

    x_left_eyes=x-width/2*0.35
    y_left_eyes=y-height/2*0.2
    x_right_eyes=x+width/2*0.35
    y_right_eyes=y-height/2*0.2
    
    # Левый глаз
    circle(screen, BLACK, (x_left_eyes,y_left_eyes), width/2*0.19, 1)
    circle(screen, RED, (x_left_eyes, y_left_eyes), width/2*0.19-1, 0)
    circle(screen, BLACK, (x_left_eyes, y_left_eyes),width/2*0.08, 0)
    line(screen, BLACK, (100,120), (175,135), 15)


    # Правый глаз
    circle(screen, BLACK, (x_right_eyes, y_right_eyes), width/2*0.14, 1)
    circle(screen, RED, (x_right_eyes, y_right_eyes), width/2*0.14-1, 0)
    circle(screen, BLACK, (x_right_eyes, y_right_eyes), width/2*0.06, 0)


pygame.init()
screen = pygame.display.set_mode((400, 400))

#Рисуем серый фон
rect(screen,LIGHTGRAY,(0,0,400,400)) 


main ()



