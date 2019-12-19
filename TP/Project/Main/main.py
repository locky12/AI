import pygame
from pygame.locals import *
from Map.map import *
from Car.car import *

run = 1
window = pygame.display.set_mode((3900,3900),RESIZABLE)
map = Map()

map.viewMap(window)

FeuRougeEVENT = USEREVENT + 1
PietonEVENT = USEREVENT + 2

pygame.time.set_timer(FeuRougeEVENT, map.timerFeuRouge)
pygame.time.set_timer(PietonEVENT, map.timerPieton)

car = Car(map,50*decalX,50*decalY)
window.blit(car.car,(car.y,car.x))

pygame.display.flip()
pygame.key.set_repeat(400, 30)

while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0

        if event.type == FeuRougeEVENT:
            map.reverseRedLightsColor()

        if event.type == PietonEVENT:
            map.generePassants()


    map.viewMap(window)
    car.carMove(1, window, map)
