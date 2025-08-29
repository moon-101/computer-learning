import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter#格式化模块

from die import Die

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#创建色子实例
die=Die()

#各结果数
x=list(range(1,die.num_sides+1))

#投一百次
results=list(die.roll() for value in range(1,101))

#计算各结果频率存表
results_count=[results.count(z) for z in x]

#导入x,y值
x_value=x
y_value=results_count

#创建图表布局
plt.style.use('ggplot')
fig,ax=plt.subplots()

#题表和轴的名称
ax.set_title('色子100次各结果频数表',fontsize=20)
ax.set_xlabel('值',fontsize=12)
ax.set_ylabel('频数',fontsize=12)


#数据可视化

ax.bar(x_value,y_value,color='blue',width=1,edgecolor='black')

#显示图表

plt.show()
