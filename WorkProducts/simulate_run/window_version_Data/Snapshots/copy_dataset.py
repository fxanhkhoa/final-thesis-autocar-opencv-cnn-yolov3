from shutil import copyfile
import time

i = 32

while True:
    try:
        filename = "dataset/" + str(i).zfill(4) + ".png"
        copyfile("fx_UIT_Car.png", filename)
        print("Saved {} successfully".format(filename))
    except:
        print("Saved {} fail".format(filename))
    time.sleep(0.5)
    i = i + 1
