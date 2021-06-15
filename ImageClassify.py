import os
import numpy as np
import cv2
import argparse
import importlib.util
import sys
import glob
from tensorflow.lite.python.interpreter import Interpreter

def result():
	os._exit(0) 

Args = argparse.ArgumentParser()
Args.add_argument('--modeldir', required=True)
Args.add_argument('--graph', default='detect.label')
Args.add_argument('--labels', default='labelmap.txt')
Args.add_argument('--image', default=None)
Args.add_argument('--imagedir', default=None)
Args.add_argument('--edgetpu', action='store_true')

a1 = Args.parse_args()
MODEL_NAME = a1.modeldir
GRAPH_NAME = a1.graph
LABELMAP_NAME = a1.labels

IM_NAME = a1.image
IM_DIR = a1.imagedir

CWD_PATH = os.getcwd()
if IM_DIR:
    PATH_TO_IMAGES = os.path.join(CWD_PATH,IM_DIR)
    images = glob.glob(PATH_TO_IMAGES + '/*')

elif IM_NAME:
    PATH_TO_IMAGES = os.path.join(CWD_PATH,IM_NAME)
    images = glob.glob(PATH_TO_IMAGES)

PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,GRAPH_NAME)
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_NAME,LABELMAP_NAME)

with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

interpreter = Interpreter(model_path=PATH_TO_CKPT)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

floating_model = (input_details[0]['dtype'] == np.float32)

input_mean = 127.5
input_std = 127.5

images="/home/pi/robotics/images/image0.jpg"
image = cv2.imread(images)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imH, imW, _ = image.shape 
image_resized = cv2.resize(image_rgb, (width, height))
input_data = np.expand_dims(image_resized, axis=0)

if floating_model:
     input_data = (np.float32(input_data) - input_mean) / input_std

interpreter.set_tensor(input_details[0]['index'],input_data)
interpreter.invoke()

boxes = interpreter.get_tensor(output_details[0]['index'])[0] 
classes = interpreter.get_tensor(output_details[1]['index'])[0]
score = interpreter.get_tensor(output_details[2]['index'])[0] 

if ((score.all() > 0.5) and (score.all()<= 1.0)):     
        ymin = int(max(1,(boxes[0][0] * imH)))
        xmin = int(max(1,(boxes[0][1] * imW)))
        ymax = int(min(imH,(boxes[0][2] * imH)))
        xmax = int(min(imW,(boxes[0][3] * imW)))
        cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)  
        object_name = labels[int(classes[0])]+" " 
        print(object_name)
        r1="turtle.write(\" "+object_name+"\")\n"
        print(r1)
        with open("/home/pi/robotics/text1.txt","a") as f1:          
             f1.write(r1)
        result()               
