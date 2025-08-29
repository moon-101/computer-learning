from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die

#创建色子实例
die_1=Die(num_sides=10)
die_2=Die()

#投色子100次
results=[]
for roll_num in range(100):
    result=die_1.roll()+die_2.roll()
    results.append(result)
print(results)

#分析结果

frequencies=[results.count(value) for value in range(2,die_1.num_sides+die_2.num_sides+1)]


print(frequencies)

# 对结果进行可视化.
x_values=list(range(1,die_1.num_sides+die_2.num_sides+1))#返回的是range对象（迭代器类型）
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={'title':'结果'}
y_axis_config={'title':'结果的频率'}
my_layout=Layout(title='资一个D6,100次结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')

