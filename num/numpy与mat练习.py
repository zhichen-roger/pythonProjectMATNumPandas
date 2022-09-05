# coding=utf-8
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rc('font', family='MicroSoft YaHei',weight='bold')
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t_us = np.loadtxt(us_file_path,delimiter=",",dtype=int)
# 取评论数数据
t_us_comments = t_us[:,-1]

# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

d = 50  #组距
num_bins = (max(t_us_comments)-min(t_us_comments))//d
print(max(t_us_comments),min(t_us_comments),max(t_us_comments)-min(t_us_comments))
print(num_bins)
plt.hist(t_us_comments,num_bins)
plt.savefig("./1.png")
plt.show()