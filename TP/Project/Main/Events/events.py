from Events import interface

class Events() :
    def __init__ () :
        pass

    def getEvenement(signalisation) :
        image = signalisation.getRandomImage()
        result = interface.Interface.predImage(image)
        return result
