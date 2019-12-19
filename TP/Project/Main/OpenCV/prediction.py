from tensorflow.keras.models import load_model
import argparse
import pickle
import cv2

from keras.applications.mobilenet import decode_predictions


PATH_MODEL = "OpenCV/output/simple_nn.model"
PATH_LABEL = "OpenCV/output/simple_nn_lb.pickle"
CLASSE_NAME = ["empty_pedestrian_crossing", "green_light","pedestrian_crossing", "red_light" , "stop"]
WIDTH  = 32
HEIGHT = 32
class Predict :


	__model = 0
	__label = 0

	def __init__(self) :
		self.__model = self.__loadModel(PATH_MODEL)
		self.__label = self.__loadLabel(PATH_LABEL)

	def __loadModel (self,pathToModel) :
		return load_model(pathToModel)


	def __loadLabel (self,pathToLabel) :
		return pickle.loads(open(pathToLabel, "rb").read())

	def __transformImageToPredict (self ,pathImage) :
		image = cv2.imread(pathImage)
		image = cv2.resize(image, (WIDTH, HEIGHT))
		image = image.astype("float") / 255.0
		image = image.flatten()
		image = image.reshape((1, image.shape[0]))
		return image


	def predict (self, pathImage) :
		image = self.__transformImageToPredict(pathImage)
		preds = self.__model.predict(image)
		i = preds.argmax(axis=1)[0]
		label = self.__label.classes_[i]
		return CLASSE_NAME[i]
