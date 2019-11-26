import pandas as pd
import time
import datetime
import random
import threading

class main_thread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
   def run(self):
        df = pd.DataFrame()
        current_time = []
        time_per_frame_main = []
        start_time = datetime.datetime.now()
        cur_time = start_time
        #random_traffic_sign_time = random.uniform(1, 12)
        #print("random traffic sign time add ", random_traffic_sign_time)
        #traffic_sign_time = datetime.timedelta(0, random_traffic_sign_time)

        #in_second = traffic_sign_time.total_seconds()
        #print("traffic sign time {} in second: {}".format(traffic_sign_time, in_second))

        #traffic_sign_detected = False
        minus_time = cur_time - start_time
        print("minus time ",minus_time)
        while minus_time < datetime.timedelta(0,12):
            time_1_frame_ran_main = random.uniform(0.033, 0.036)
            current_time.append(minus_time.total_seconds())
            time_per_frame_main.append(1/time_1_frame_ran_main)
            minus_time = datetime.datetime.now() - start_time
            print("time ran: {}".format(minus_time))
            time.sleep(time_1_frame_ran_main)
        df['current_time_main'] = current_time
        df['frame_processing_main'] = time_per_frame_main
        export_csv = df.to_csv ("data_main_thread.csv", index = None, header=True) #Don't forget to add '.csv' at the end of the path

        print (df)
        