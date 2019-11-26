import shutil
import sys
from os import path
import time
import os

src_path = sys.argv[1]
dst_path = sys.argv[2]

for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(".xml"):
            print(os.path.join(root, file), "moved")
            shutil.move(os.path.join(root, file), 
                        os.path.join(dst_path, file))