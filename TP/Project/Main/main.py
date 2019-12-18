import pygame
from pygame.locals import *
from Map.map import *
from Car.car import *
# from Car.listCar import *

run = 1
window = pygame.display.set_mode((3900,3900),RESIZABLE)
map = Map()
#dessine la map
map.viewMap(window)
#evenement d'inversion des feux rouges et pietons
FeuRougeEVENT = USEREVENT + 1
PietonEVENT = USEREVENT + 2
#on definit les timers
pygame.time.set_timer(FeuRougeEVENT, map.timerFeuRouge)
pygame.time.set_timer(PietonEVENT, map.timerPieton)

car = Car(map,50*decalX,50*decalY)
window.blit(car.car,(car.y,car.x))# colle image à la position x et y
# car1 = Car(map,300,50)
# window.blit(car1.direction,(car1.x,car1.y))
# list = ListCar(map)
# list.createRandCars()
# list.print_all_cars(window)

pygame.display.flip() # rafraichit l'ecran
pygame.key.set_repeat(400, 30)
# pygame.time.Clock().tick(1)

while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0

        #inversion des feux rouges
        if event.type == FeuRougeEVENT:
            map.reverseRedLightsColor()

        #generation des pietons
        if event.type == PietonEVENT:
            map.generePassants()

        # mouvement
        if event.type == KEYDOWN:
            if event.key == K_UP:
                map.positionX += 50
            if event.key == K_RIGHT:
                map.positionY -= 50
            if event.key == K_DOWN:
                map.positionX -= 50
            if event.key == K_LEFT:
                map.positionY += 50

    # # print(car.x, car.y)


    map.viewMap(window)
    # list.print_all_cars(window)
    car.randomMove(window, map)
    car.printCar(window)
    # window.blit(car.direction,(car.x,car.y))

    #pygame.display.flip()
    # pygame.time.Clock().tick(30)
