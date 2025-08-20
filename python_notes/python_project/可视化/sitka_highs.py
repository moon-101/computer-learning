import csv
from datetime import datetime

from matplotlib.ticker import FuncFormatter#格式化模块
import matplotlib.pyplot as plt




# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#获得日期和温度数据
file_name=r'data\sitka_weather_2021_simple.csv'
with open(file_name) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    for index,column_header in enumerate(header_row):
        print(index,header_row)
    
    dates=[]
    highs=[]

    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        dates.append(current_date)
        highs.append(high)
print(highs)
print("可用样式列表:", plt.style.available)

#生成图表
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red')

#美化图表
plt.style.use('seaborn-v0_8-pastel')
ax.set_title('2021年每日最高温度',fontsize=24)
fig.autofmt_xdate()
ax.set_xlabel('日期',fontsize=16)
ax.set_ylabel('温度',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

#展示图表
plt.show()
