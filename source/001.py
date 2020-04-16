import matplotlib.pyplot as plt
import random
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(120)
random.seed(10)
y = [random.randint(20, 35) for i in range(120)]
plt.plot(x, y)

_xtick_lables = ['10点{}分'.format(i) for i in range(60)]
_xtick_lables += ['11点{}分'.format(i) for i in range(60)]

# 取步长，一共120个点，步长为3，只取40个，第一个参数是数字，第二个参数是字符串，一一对应
# 以最右边对其旋转45度，并设置本地字体，解决中文乱码问题
plt.xticks(list(x)[::3], _xtick_lables[::3], rotation=45, ha='right', fontproperties=my_font)

plt.show()
