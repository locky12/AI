
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from imutils import paths
import numpy as np
import random
import pickle
import cv2
import os


def LoadImageAndLabel () :
    data = []
    labels = []
    imagePaths = sorted(list(paths.list_images("./images")))
    random.seed(42)
    random.shuffle(imagePaths)

    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        if image is not None:
            image = cv2.resize(image, (32, 32)).flatten()
            data.append(image)
            label = imagePath.split(os.path.sep)[-2]
            labels.append(label)
    labels = np.array(labels)
    data = np.array(data, dtype="float") / 255.0
    return data,labels


def separateData ():
    data, labels = LoadImageAndLabel()
    (trainX, testX, trainY, testY) = train_test_split(data,
        labels, test_size=0.25, random_state=42)

    lb = LabelBinarizer()
    trainY = lb.fit_transform(trainY)
    testY = lb.transform(testY)
    return lb,trainX, trainY, testX, testY

def initModel (lb) :
    model = Sequential()
    model.add(Dense(1024, input_shape=(3072,), activation="sigmoid"))
    model.add(Dense(512, activation="sigmoid"))
    model.add(Dense(len(lb.classes_), activation="softmax"))
    return model



def compileModelandPred () :
    INIT_LR = 0.01
    EPOCHS = 75
    lb,trainX, trainY, testX, testY = separateData ()
    model = initModel (lb)



    opt = SGD(lr=INIT_LR)
    model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

    H = model.fit(trainX, trainY, validation_data=(testX, testY),validation_split=0.25,
        epochs=75, batch_size=32)
    predictions = model.predict(testX, batch_size=32)
    print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=lb.classes_))
    model.save("output/simple_nn.model")
    f = open("output/simple_nn_lb.pickle", "wb")
    f.write(pickle.dumps(lb))
    f.close()

compileModelandPred ()
