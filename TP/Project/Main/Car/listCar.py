from car import *
import random
MOVE = 0.1
nb_img = 50
position_depart = [[50,50],[300,50],[50,300]]
liste_deplacement = ["droite","gauche","haut","bas","reste"]
class ListCar():
    def __init__ (self,map):
        self.list = []
        self.map = map

    def add_car (self,car):
        self.list.append(car)

    def print_all_cars(self,window):
        for car in self.list :
            window.blit(car.car,(car.x,car.y))
        pygame.display.flip()

    def calc_new_cord (self,window):
        for i in range(nb_img):
            for car in self.list :
                # print(car.direction)
                if (car.direction == "droite"):
                    # print("ok : ", car.x)
                    car.x += 50#(car.distance/nb_img)
                if (car.direction == "gauche"):
                    car.x -= (car.ditance/nb_img)
                if (car.direction == "haut"):
                    car.y += (car.distance/nb_img)
                if (car.direction == "bas"):
                    car.y -= (car.distance/nb_img)
                window.blit(car.car,(car.x,car.y))
                pygame.display.flip()
    # def move_all_cars (nb_case,window):

    def createRandCars (self):
        for i in position_depart :
            car = Car(i[0],i[1])
            self.add_car(car)

    def move_all_cars_x(self, x):
        for  car in self.list :
            car.x += x

    def move_all_cars_y(self, y):
        for  car in self.list :
            car.y += y

    def deplacementAlea (self):
        for car in self.list:
            r = random.randint(0,4)
            print("l :", liste_deplacement[r])
            car.deplacement = liste_deplacement[r]
    def mouvement (self,window):
        self.deplacementAlea()
        self.calc_new_cord(window)
