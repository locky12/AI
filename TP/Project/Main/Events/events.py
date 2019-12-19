from Events import interface

class Events() :
    def __init__ () :
        pass

    def getEvenement(signalisation) :
        image = signalisation.getRandomImage()
        # print(image)
        result = interface.Interface.predImage(image)
        # result = signalisation.getFonction()
        return result
