import csv
from datetime import datetime

from matplotlib.ticker import FuncFormatter#格式化模块
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


filename=r'data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    print(header_row[5])
    #从文件中获取日期、最高温度和最低温度
    datas,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[4])
        low=int(row[5])
        datas.append(current_date)
        highs.append(high)
        lows.append(low)
        
#根据最高温度和最低温度绘制图形
plt.style.use('seaborn-v0_8-pastel')
fig,ax=plt.subplots()
ax.plot(datas,highs,c='red',alpha=0.5)
ax.plot(datas,lows,c='blue',alpha=0.5)
ax.fill_between(datas,highs,lows,facecolor='blue',alpha=0.1)

#设置图形的格式
ax.set_title('2021年每日温度',fontsize=24)

plt.show()