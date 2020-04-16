from matplotlib import pyplot as plt
from matplotlib import font_manager

'''
绘制条形图
条形图:排列在工作表的列或行中的数据可以绘制到条形图中。
特点:绘制连离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计)
'''

# 设置中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

fig = plt.figure(figsize=(20, 8), dpi=80)

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

# # 绘制条形图
# plt.bar(range(len(a)), b, width=0.3)
# # 设置字符串到x轴
# plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=90)

# 绘制横向的条形图: y轴显示电影名称，x轴显示票房，初始化时，先将y轴使用20个(电影总个数)数字填充，后面再替换成电影名称
plt.barh(range(len(a)), b, height=0.5, color="orange")
# 设置字符串到y轴
plt.yticks(range(len(a)), a, fontproperties=my_font)

# plt.xticks(list(range(int(max(b))+10))[::10])

plt.grid(alpha=0.4)

plt.show()
