import matplotlib.pyplot as plt#导入函数
from matplotlib.ticker import FuncFormatter#格式化模块

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values=range(-100,101)
y_values=[x**2+1 for x in x_values]

plt.style.use('ggplot')
fg,ax=plt.subplots()

#题表和轴的名称
ax.set_title('平方函数',fontsize=20)
ax.set_xlabel('x',fontsize=12)
ax.set_ylabel('y',fontsize=12)

#绘点
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=10)#类的应用



"""#显示
plt.show()
"""
#存储
plt.savefig('squaress函数_plot.png')