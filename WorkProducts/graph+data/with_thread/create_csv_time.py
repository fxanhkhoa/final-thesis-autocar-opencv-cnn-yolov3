import pandas as pd
import time
import datetime
import random
import threading
import matplotlib.pyplot as plt

from sub_thread.thread_main import main_thread
from sub_thread.thread_detect_line import detect_line_thread
from sub_thread.thread_traffict_sign import traffic_sign_thread

df = pd.DataFrame()

# Create new threads
thread_main_run = main_thread()
thread_detect_line_run = detect_line_thread()
thread_traffic_sign_run = traffic_sign_thread()

thread_main_run.start()
thread_detect_line_run.start()
thread_traffic_sign_run.start()

time.sleep(14)
df_main = pd.read_csv('data_main_thread.csv')
df_detect_line = pd.read_csv('data_detect_line_thread.csv')
df_traffic_sign = pd.read_csv('data_traffic_sign_thread.csv')

ax = plt.gca()

df_main.plot(kind='line',x='current_time_main',y='frame_processing_main',ax=ax)
df_detect_line.plot(kind='line',x='current_time_detect_line',y='frame_processing_detect_line',ax=ax)
df_traffic_sign.plot(kind='line',x='current_time_traffic_sign',y='frame_processing_traffic_sign',ax=ax)

plt.show()
print("exit main thread")