# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

#rating,runtime分布情况
#选择图形，直方图
#准备数据
runtime_data = df["Rating"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
print(min_runtime,max_runtime)
#计算组数
print(max_runtime-min_runtime)
#设置不等宽的组距，hist方法中取到的会是一个左闭右开的去见[1.9,3.5)
num_bin_list = [1.9,3.5]
i=3.5
while i<=max_runtime:
    i += 0.5
    num_bin_list.append(i)
print(num_bin_list)



#设置图形的大小
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin_list)

plt.xticks(num_bin_list)


plt.show()