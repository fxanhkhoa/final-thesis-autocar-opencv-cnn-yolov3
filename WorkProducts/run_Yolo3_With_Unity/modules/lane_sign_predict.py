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
from tqdm import tqdm
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
        ret = "NONE"

        with open(self.config_path) as config_buffer:    
            config = json.load(config_buffer)

        makedirs(self.output_path)

        return ret
