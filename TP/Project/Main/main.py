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
#evenement d'inversion des feux rouges
SignalisationsEVENTS = USEREVENT + 1
#on definit le timer
pygame.time.set_timer(SignalisationsEVENTS, map.Timer)

car = Car(map,50,50)
window.blit(car.car,(car.x,car.y))# colle image à la position x et y
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
        if event.type == SignalisationsEVENTS:
            map.reverseRedLightsColor()
            map.generePassants()

        # mouvement
        if event.type == KEYDOWN:
            if event.key == K_UP:
                map.positionY += 50
                # list.move_all_cars_y(-50)
            if event.key == K_DOWN:
                map.positionY -= 50
                # list.move_all_cars_y(+50)
            if event.key == K_LEFT:
                map.positionX += 50
                # list.move_all_cars_x(+50)
            if event.key == K_RIGHT:
                map.positionX -= 50
                # list.move_all_cars_x(-50)
                # car.x -=50

    # # print(car.x, car.y)


    map.viewMap(window)
    # list.print_all_cars(window)
    car.randomMove(window, map)
    car.printCar(window)
    # window.blit(car.direction,(car.x,car.y))

    #pygame.display.flip()
    # pygame.time.Clock().tick(30)
