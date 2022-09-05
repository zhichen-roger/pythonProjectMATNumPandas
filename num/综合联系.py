# coding=utf-8
import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
# 加载国家数据
us_data = np.loadtxt(us_file_path,delimiter=",",dtype=int)
uk_data = np.loadtxt(uk_file_path,delimiter=",",dtype=int)
# 添加国家信息
# 构造全为0的数据
zero_data = np.zeros((us_data.shape[0],1)).astype(int)
one_data = np.ones((uk_data.shape[0],1)).astype(int)
# print(zero_data)
# 分别添加一列数据
us_data = np.hstack((us_data,zero_data))
uk_data = np.hstack((uk_data,one_data))
# 拼接两组数据
final_data = np.vstack((us_data,uk_data))
# print(final_data)
# 将所有值为1 替换为-1
# final_data[t==1]=-1
# 横方向axis=0   纵方向为axis=1 最大值
# np.argmax(final_data,axis=0)
# 4h5l 10-20的整数
# np.random.randint(10,20,(4,5))
# 随机种子
np.random.seed(10)
t = np.random.randint(0,20,(4,5))
print(t)