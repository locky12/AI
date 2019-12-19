import sys
sys.path.append("..")

from OpenCV import prediction

class Interface :


    def __init__ () :
        pass


    def predImage (pathImage) :
        pred = prediction.Predict()
        result  = pred.predict(pathImage)
        print("result : " , result)
        if result == "red_light" :
            return "red"
        if result == "green_light" :
            return "green"
        if result == "stop" :
            return "stop"
        if result == "empty_pedestrian_crossing":
            return "empty"
        if result == "pedestrian_crossing":
            return "pedestrian"

#
# r = Interface.predImage("fr.jpg")
# print(r)
