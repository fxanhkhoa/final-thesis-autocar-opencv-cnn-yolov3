import shutil
import sys
from os import path
import time
import os
import xml.etree.ElementTree as ET

src_path = sys.argv[1]
dst_path = sys.argv[2]

for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(".xml"):
            tree = ET.parse(os.path.join(root, file))
            xmlroot = tree.getroot()
            found = 0
            for eachobject in xmlroot.findall('object'):
                if (eachobject[0].text == 'NoLeft' or 
                    eachobject[0].text == 'NoRight'):
                    found = 1
                    break
            if (found == 0):
                os.remove(os.path.join(root, file))
                print(os.path.join(root, file), "removed")
                png_name = file.replace('xml', 'png')
                os.remove(os.path.join(root, png_name))
                print(os.path.join(root, png_name), "removed")