import  matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.style.use('ggplot')
fig,ax=plt.subplots()
ax.plot(squares,linewidth=3)

#设置图表标题并给坐标轴加上标签。
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)



# 绘制一个点
ax.scatter([1,2,3,4],[1,2,3,4])

#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)

plt.show()