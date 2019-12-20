import sys
sys.path.append("..") # Adds higher directory to python modules path.

import os
import argparse
import json
import cv2
from utils.utils import get_yolo_boxes, makedirs
from utils.bbox import draw_boxes
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from keras.models import load_model
import numpy as np

class lane_trafficsign:
    def __init__(
        self, 
        id,
        config_path,
        input_path,
        output_path
        ):
        self.id = id
        self.config_path = config_path
        self.input_path = input_path
        self.output_path = output_path

    def predict(self, pic):
        ret = []

        with open(self.config_path) as config_buffer:    
            config = json.load(config_buffer)

        makedirs(self.output_path)

        ###############################
        #   Set some parameter
        ###############################       
        net_h, net_w = 416, 416 # a multiple of 32, the smaller the faster
        obj_thresh, nms_thresh = 0.7, 0.45

        ###############################
        #   Load the model
        ###############################
        os.environ['CUDA_VISIBLE_DEVICES'] = config['train']['gpus']
        infer_model = load_model(config['train']['saved_weights_name'])

        image_paths = []
        if os.path.isdir(self.input_path): 
            for inp_file in os.listdir(self.input_path):
                image_paths += [self.input_path + inp_file]
        else:
            image_paths += [self.input_path]

        image_paths = [inp_file for inp_file in image_paths if (inp_file[-4:] in ['.jpg', '.png', 'JPEG'])]

        # the main loop
        # for image_path in image_paths:
        image = cv2.imread(pic)
        print(pic)

        # predict the bounding boxes
        boxes = get_yolo_boxes(infer_model, 
                                [image], 
                                net_h, 
                                net_w, 
                                config['model']['anchors'], 
                                obj_thresh, 
                                nms_thresh)[0]
        for box in boxes:
            for i in range(len(config['model']['labels'])):
                if box.classes[i] > obj_thresh:
                    ret.append([config['model']['labels'][i], box.classes[i]])
                    print(config['model']['labels'][i], " ", box.classes[i])

        # draw bounding boxes on the image using labels
        draw_boxes(image, boxes, config['model']['labels'], obj_thresh) 
    
        # write the image with bounding boxes to file
        print("file save to {}".format(self.output_path + pic.split('/')[-1]))
        cv2.imwrite(self.output_path + pic.split('/')[-1], np.uint8(image))

        return ret
