import matplotlib
from matplotlib import pyplot as plt
import random

matplotlib.rc('font', family='MicroSoft YaHei',weight='bold')
fig  = plt.figure(figsize=(20,8),dpi=80)
x = range(0,120)
y=[random.randint(20,35) for i in range(120)]
plt.plot(x,y)
# 绘制x轴刻度

_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)
plt.xlabel('时间')
plt.ylabel('温度℃')
plt.title('温度变化情况')
# 绘制网格 透明度alpha
plt.grid(alpha = 0.4)
plt.savefig('./2.png')
plt.show()