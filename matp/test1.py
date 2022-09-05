from matplotlib import pyplot as plt
fig  = plt.figure(figsize=(20,8),dpi=80)
x = range(2,26,2)
y=[15,13,14.5,17,28,25,26,26,24,22,18,15]
plt.plot(x,y)
# 绘制x轴刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels)
plt.yticks(range(min(y),max(y)+10))
plt.savefig('./1.png')
plt.show()