from matplotlib import pyplot as plt
from matplotlib import font_manager

'''
绘制折线图
折线图:以折线的上升或下降来表示统计数量的增减变化的统计图
特点:能够显示数据的变化趋势，反映`事物的变化情况。(变化)
'''

# 设置中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 设置线条的label，颜色，样式效果
plt.plot(x, y_1, label='自己', color='orange', linestyle=':')
plt.plot(x, y_2, label='同桌', color='cyan', linestyle='-.')

# 设置x轴显示的文字，一共20个，11岁, 12岁, ... , 31岁
_xtick_lables = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_lables, fontproperties=my_font)

plt.xlabel('年龄', fontweight='bold', fontproperties=my_font)
plt.ylabel('数量', fontweight='bold', fontproperties=my_font)
plt.title('朋友个数统计图',fontsize=16, fontweight='bold', fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.5)
# 绘制图例
plt.legend(prop=my_font, loc='upper left')

plt.show()
