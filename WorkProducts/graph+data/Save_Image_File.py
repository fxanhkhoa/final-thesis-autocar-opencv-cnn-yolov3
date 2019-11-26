import shutil
import sys
from os import path
import time

src_path = sys.argv[1]
dst_path = sys.argv[2]

i = 1

print(src_path, dst_path)

while (True):
   filename = dst_path + "\\" + str(i).zfill(4) + ".png"
   while path.exists(filename):
      i = i + 1
      filename = dst_path + "\\" + str(i).zfill(4) + ".png"
      
   try:
      shutil.copy2(src_path + "\\" + "fx_UIT_Car.png", filename)
      print(filename, " Saved")
   except:
      print(filename, " Failed")

   time.sleep(0.5)