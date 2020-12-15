import csv
import pygame
import os
import time
from math import sqrt
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((800, 600))
score = 0
lose = 0
ball = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def save_hiscore():
    '''
    Функция читает из файла таблицу рекордов.
    Добавляет новые результаты в таблицу
    Выводит таблицу на экран
    Записывает в файл новые результаты.
    '''
    #Читаем таблицу из файла
    try:
        with open('hiscore.txt', newline='') as file:
            hiscore = list(csv.reader(file))      # read rows
    except:
        hiscore=[]
        
    # Добавляем текущие результаты , добавляем флаг один, что это новая запись
    hiscore.append(['Player',str(score),'1'])
    hiscore=sorted(hiscore,key=lambda x: int(x[1]),reverse=True)

    #Выводим результаты на экран
    j=0
    for i in hiscore[0:10]:
        f1 = pygame.font.Font(None, 30)
        j+=1
        # Если новый результат - печатаем зеленым 
        if i[2]=='1':
            text2 = f1.render(str(j)+' '+' '.join(i[0:2]), 1, (0, 255, 0))
            hiscore[j-1][2]='0' # Делаем результат старым
        else:
            text2 = f1.render(str(j)+' '+' '.join(i[0:2]), 1, (255, 0, 0))
        screen.blit(text2,(80,20+j*33))
        pygame.display.update()
        
    pause_anykey()
    
    #Записываем новую таблицу в файл
    with open('hiscore.txt', 'w', newline='') as file:
        csv.writer(file).writerows(hiscore)   # write rows


def pause_anykey ():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
               return



def new_ball():
    ''' Функция рисует шарик '''
    global x, y, r
    global ball,Ball
    # Создаем список с параметрами шаров 
    Ball = [[] * 3 for i in range(ball)]
    
    for i in range(ball):
        x = randint(100,700)
        y = randint(100,500)
        r = randint(30,50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        Ball[i]=x,y,r
        
def click(event):
    ''' Обрабатываем событие на нажатие мыши'''
    ''' Попал или не попал в шарик '''
    global score,lose,FPS

    if popadanie_v_krug (event):
        score+=1
    else :
        lose+=1

   #Условие окончания игры
    if lose == 1:
        save_hiscore()
        pygame.quit()

    #Ускорение игры
    if score%3 == 0:
        FPS+=0.1


def mwin ():
    # Если победа.
    f1 = pygame.font.Font(None, 60)
    text1 = f1.render("Настоящий тигр!", 1, GREEN)
    text2 = f1.render("Победа!", 1, GREEN)  

    screen.blit(text1,(50,200))
    screen.blit(text2,(50,280))
    pygame.display.update()
    pause_anykey ()

def mlose ():

    # Если проиграл.    
    f1 = pygame.font.Font(None, 60)
    text1 = f1.render("Кулема!", 1, RED)
    text2 = f1.render("Проиграла!", 1, RED)  

    screen.blit(text1,(50,200))
    screen.blit(text2,(50,280))
    pygame.display.update()
    pause_anykey ()


def popadanie_v_krug (event):
    '''
    Функция принимает событие мыши и смотрит попал клил мыши в круг.
    Если попал возвращает 1, если нет 0
    '''
    global Ball,ball
    for i in range(ball):
        x,y,r=Ball[i]
        mouse_x,mouse_y=event.pos
        del_x=mouse_x-x
        del_y=mouse_y-y
        del_r=sqrt(del_x**2+del_y**2)

        if del_r<=r :
             return 1

    return 0

def draw_score ():
    '''
    Выводит на экран счет
    '''
    
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render("Очки:", 1, (255, 0, 0))
    text2 = f1.render(str(score), 1, (255, 0, 0))
    screen.blit(text1,(0,0))
    screen.blit(text2,(80,0))

    text3 = f1.render("Мимо:", 1, (255, 0, 0))
    text4 = f1.render(str(lose), 1, (255, 0, 0))
    screen.blit(text3,(0,20))
    screen.blit(text4,(80,20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball()
    draw_score()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
