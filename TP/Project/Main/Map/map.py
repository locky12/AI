import pygame
from pygame.locals import *
import constante as const
import Signilisation.feuRouge as FR
import Signilisation.panneauStop as STOP
import Signilisation.passagePieton as PP

tailleCase = 50
RED = (255,0,0)
GREEN = (0,255,0)
hashmap = { "0" : "routeSimple",
            "8" : "routeHH",
            "2" : "routeHB",
            "6" : "routeVD",
            "4" : "routeVG" ,
            "b" : "building",
            "_" : "carreNoir",
            "u" : "routeHH",
            "n" : "routeHB",
            "k" : "routeVD",
            "h" : "routeVG",
            "z" : "pietonHH",
            "w" : "pietonHB",
            "d" : "pietonVD",
            "q" : "pietonVG",
            "p" : "routeHH",
            ":" : "routeHB",
            "ù" : "routeVD",
            "l" : "routeVG"}

class Map :

    class Case:
        def __init__(self,char):
            self.char = char
            self.type = ""
            self.signalisation = 0

    def __init__(self):
        self.matrix = 0
        self.positionX = -50
        self.positionY = 0
        self.images = dict()
        self.timerFeuRouge = 5000 # = 5 secondes
        self.timerPieton = 2000 # = 2 secondes
        self.__genereMap()

    def viewMap(self, window) :

        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionY
                y = num_row * const.taille_case + self.positionX

                window.blit(self.images["carreNoir"],(x,y))
                window.blit(self.images[hashmap[case.char]],(x,y))

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

        self.__drawSignalisations(window)

    def generePassants(self):
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                if case.type == "pieton" :
                    case.signalisation.generePieton()


    def reverseRedLightsColor(self):
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                if case.type == "feu" :
                    if case.signalisation.color == RED :
                        case.signalisation.color = GREEN
                    else :
                        case.signalisation.color = RED

    def __drawSignalisations(self, window):
        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionY
                y = num_row * const.taille_case + self.positionX

                if case.type == "stop" :
                    window.blit(self.images["stop"],(x+15,y+15))

                if case.type == "feu" :
                    case.signalisation.printFeuRouge(window, x, y)

                if case.type == "pieton":
                    if case.signalisation.passants == 1:
                        window.blit(self.images["pieton"],(x,y))

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

    def __genereMap (self) :
        self.__initDict()

        with open("./Data/Map/map.txt", "r") as file:
            struct = []
            for row in file :
                row_struct = []
                for s in row:
                    if s != "\n" :
                        case = self.Case(s)
                        row_struct.append(case)
                struct.append(row_struct)

        self.matrix = struct
        self.__initSignalisations()

    def __initSignalisations(self) :
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                if case.char == "u" or case.char == "n":
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(RED)
                if case.char == "k" or case.char == "h":
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(GREEN)
                if case.char == "z" or case.char == "w" or case.char == "d" or case.char == "q" :
                    case.type = "pieton"
                    case.signalisation = PP.PassagePieton()
                if case.char == "p" or case.char == "ù" or case.char == ":" or case.char == "l" :
                    case.type = "stop"
                    case.signalisation = STOP.Stop()

    def __initDict(self):
        self.images["herbe"] = pygame.transform.scale(pygame.image.load("./Data/Images/herbe.jpg").convert(), (1900, 1000))

        self.images["eau"] = pygame.image.load("./Data/Images/eau.jpg").convert()

        self.images["carreNoir"] = pygame.transform.scale(pygame.image.load("./Data/Images/carreNoir.jpg").convert(), (tailleCase, tailleCase))

        self.images["building"] = pygame.transform.scale(pygame.image.load("./Data/Images/home.png").convert_alpha(), (tailleCase, tailleCase))
        # carrefour
        self.images["routeSimple"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeSimple.jpg").convert(), (tailleCase, tailleCase))
        #route horizontal haut
        self.images["routeHH"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeHorizontalH.jpg").convert(), (tailleCase, tailleCase))
        #route horizontal bas
        self.images["routeHB"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeHorizontalB.jpg").convert(), (tailleCase, tailleCase))
        #route vertical gauche
        self.images["routeVG"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeVerticalG.jpg").convert(), (tailleCase, tailleCase))
        # route vertical droite
        self.images["routeVD"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeVerticalD.jpg").convert(), (tailleCase, tailleCase))
        #pieton horizontal haut
        self.images["pietonHH"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonHorizontalH.jpg").convert(), (tailleCase, tailleCase))
        #pieton horizontal bas
        self.images["pietonHB"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonHorizontalB.jpg").convert(), (tailleCase, tailleCase))
        #pieton vertical gauche
        self.images["pietonVG"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonVerticalG.jpg").convert(), (tailleCase, tailleCase))
        #pieton vertical droite
        self.images["pietonVD"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonVerticalD.jpg").convert(), (tailleCase, tailleCase))
        #panneau stop
        self.images["stop"] = pygame.transform.scale(pygame.image.load("./Data/Images/panneauStop.png").convert(), (tailleCase-25, tailleCase-25))
        #pieton
        self.images["pieton"] = pygame.transform.scale(pygame.image.load("./Data/Images/homme.png").convert_alpha(), (tailleCase, tailleCase))
