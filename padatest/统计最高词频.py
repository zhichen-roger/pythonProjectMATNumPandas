import numpy as np
import pandas as pd
df = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())
# 排序
df = df.sort_values(by='Count_AnimalName',ascending=False)
print(df)
# 去前20行某一列
# 方括号写数组，表示取行，对行进行操作
# 写字符串，表示的取列索引，对列进行操作
# print(df[:20])
# print(df['Row_Labels'])
print(df[(800<df['Count_AnimalName'])&(df['Count_AnimalName']<1000)])