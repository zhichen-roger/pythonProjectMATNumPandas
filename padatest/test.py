import numpy as np
import pandas as pd
t = pd.Series([1,2,3,4,5],index=list('abcde'))
t = t.astype(float)
# print(t)
# print(t['a'])
# print(t[1])
# print(t[['a','c']])
# print(t[[1,3]])
# 打印序列 也就是key值
# print(t.index)

t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list("WXYZ"))
print(t1)

d1 = {"name":["xiaomig","xiaolan"],"age":[20,32],"tel":[10086,10010]}
t2 = pd.DataFrame(d1)
print(t2)

d2 = [{"name":"xiaohong","age":32,"te1":10010},{"name":"xiaogang","tel":10000},{"name":"xiaowang","age":22}]
t3 = pd.DataFrame(d2)
print(t3)

# 显示头几行 默认前5行
print(t3.head(1))
# 显示尾几行 默认前5行
print(t3.tail(2))
# 展示概览
print(t3.info())
# 快速进行数字统计
print(t3.describe())