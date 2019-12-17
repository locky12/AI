# USAGE
# python prediction.py --image fr.jpg --model output/simple_nn.model --label-bin output/simple_nn_lb.pickle --width 32 --height 32 --flatten 1
# python predict.py --image images/dog.jpg --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --width 64 --height 64

# import the necessary packages
from tensorflow.keras.models import load_model
import argparse
import pickle
import cv2

from keras.applications.mobilenet import decode_predictions
#from tabulate import tabulate

PATH_MODEL = "output/simple_nn.model"
PATH_LABEL = "output/simple_nn_lb.pickle"
CLASSE_NAME = ["green_light", "pedestrian_crossing_empty", "red_light", "stop"]
class Predict :
	__width  = 32
	__height = 32
	__imageOutput = 0
	__model = 0
	__label = 0

	def __init__(self) :
		self.__model = self.__loadModel(PATH_MODEL)
		print(self.__model)
		self.__label = self.__loadLabel(PATH_LABEL)

	def __loadModel (self,pathToModel) :
		print(pathToModel)
		return load_model(pathToModel)


	def __loadLabel (self,pathToLabel) :
		return pickle.loads(open(pathToLabel, "rb").read())

	def __transformImageToPredict (self ,pathImage) :
		image = cv2.imread(pathImage)
		output = image.copy()
		image = cv2.resize(image, (self.__width, self.__height))
		image = image.astype("float") / 255.0
		image = image.flatten()
		image = image.reshape((1, image.shape[0]))
		return image, output


	def predict (self, pathImage) :
		image, output = self.__transformImageToPredict(pathImage)
		preds = self.__model.predict(image)
		i = preds.argmax(axis=1)[0]
		label = self.__label.classes_[i]
		text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
		cv2.putText(output, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
			(0, 0, 255), 2)
		for j in range(4) :
			print(CLASSE_NAME[j]," : ",preds[0][j])
		# show the output image
		# cv2.imshow("Image", output)
		# cv2.waitKey(0)
		return CLASSE_NAME[i]
		# print (tabulate(decode_predictions(preds, top=5)[0], headers=['Name', 'Probability']))




predition = Predict()
r = predition.predict("fr.jpg")
print(r)
