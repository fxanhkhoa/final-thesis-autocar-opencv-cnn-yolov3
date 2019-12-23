import pandas as pd
import time
import datetime
import random

df = pd.DataFrame()

current_time = []
time_per_frame = []

# current_time.append(1.2323)
# time_per_frame.append(2.333)

start_time = datetime.datetime.now()
cur_time = start_time
random_traffic_sign_time = random.uniform(1, 12)
print("random traffic sign time add ", random_traffic_sign_time)
traffic_sign_time = datetime.timedelta(0, random_traffic_sign_time)

in_second = traffic_sign_time.total_seconds()
print("traffic sign time {} in second: {}".format(traffic_sign_time, in_second))

traffic_sign_detected = False

## 0.041 -> 0.042 ---- 24 frames
## 0.052 -> 0.055 ---- 18 frames
minus_time = cur_time - start_time
print("minus time ",minus_time)
while minus_time < datetime.timedelta(0,12):
    if ((minus_time > traffic_sign_time) and 
        (traffic_sign_detected == False)):
        traffic_sign_detected = True
        time_1_frame_ran = random.uniform(0.052, 0.055)
        print("===== THIS TIME TRAFFIC SIGN {} ======"
        .format(time_1_frame_ran))
    else:
        time_1_frame_ran = random.uniform(0.041, 0.042)
    current_time.append(minus_time.total_seconds())
    time_per_frame.append(1/time_1_frame_ran)
    minus_time = datetime.datetime.now() - start_time
    print("time ran: {}".format(minus_time))
    time.sleep(time_1_frame_ran)
    

df['current_time'] = current_time
df['frame_processing'] = time_per_frame

export_csv = df.to_csv ("data_YOLO.csv", index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)