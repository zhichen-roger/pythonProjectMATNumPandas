# coding=utf-8
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rc('font', family='MicroSoft YaHei',weight='bold')
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype=int)
# 选择比50000小的数据
t_uk = t_uk[t_uk[:,1]<=50000]

# 取评论数数据和喜欢数数据
t_uk_comments = t_uk[:,-1]
t_uk_like = t_uk[:,1]

plt.scatter(t_uk_like,t_uk_comments)