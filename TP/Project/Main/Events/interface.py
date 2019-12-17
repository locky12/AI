import sys
sys.path.append("..")

from OpenCV import prediction

class Interface :


    def __init__ () :
        pass


    def predImage (pathImage) :
        pred = prediction.Predict()
        result  = pred.predict(pathImage)
        if result == "red_light" :
            return "stop"
        if result == "green_light" :
            return "continue"
        if result == "stop" :
            return "stop"
        if result == "empty_pedestrian_crossing"
            return "continue"
        if result == "pedestrian_crossing"
            return "stop"


r = Interface.predImage("fr.jpg")
print(r)
