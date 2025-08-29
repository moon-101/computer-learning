# 数据可视化
* 数据可视化是什么?
指的是通过可视化表示来探索数据。#说得跟没说一样,我个人理解:数据转化为几何图形表示,如同数学上的数形结合,从而更容易看到数据中蕴含的规律。也利于数据分析。
# 两种常见的文件类型
## CSV文件
1. csv文件长什么样子的?如何判断一个文件是否是csv文件?csv文件有什么特征?
A:要在文本文件中存储数据,一个简单方式是将数据以逗号分隔,这样的形式称为csv文件,csv文件内部文件结构长得像矩阵,一列一行排布的?通常可以从文件名后缀可以看出是否csv文件,当然还可以从文件内部可以看出,但属实有点蛋疼.如前言所说,csv文件特征是,文件名后缀,文件内部结构如同矩阵.
2. csv文件如何使用?提取csv文件中想要的信息
简单示例:
    import csv#导入csv库
    with open(file_name) as f: #打开csv文件
        reader=csv.reader(f) #调用csv文件reader方法
        head_row=next(reader) #next函数可以读取csv文件中的下一行数据
    
    for index,column_header in enumerate(header_row):#enumerate函数,对有限循环次数计数
        print(index,columu_header)
    
    dates=[]
    highs=[]
    #开始读取存储目标数据
    for row in reader:
        current_date=datetime.strptime(row[2],"%Y-%m-%d)
        high=int(row[5])
        dates.append(current_date)
        highs.append(high)

## json文件
1. json文件是什么东西?json文件一大特征是让人看不懂,纷繁错杂。它是给机器看的，对于我们要处理它，要用到专门的工具，json库
如何解读json文件
    
    import json #导入相关库
    file_name=''
    with open(file_name) as f:
        data=json.load(f)#json.load()将数据转换为python能够处理的格式
    
    new_file=''
    with open(new_file,'w'):
        json.dump(data,new_file,indent=4)#json.dump()接受一个JSON数据对象和一个文件对象,并将json数据对象写入该文件对象,参数indent=4让dump()使用与数据结构相匹配的缩进量来设置数据的格式.
2. 提取json目标信息

    mubiao_data=data['features']
    mags=[]
    for eq_dict in mubiao_data:
        mag=eq_dict['properties']['mag']
        mags.append(mag)
    print(mags[:10])



# 常用的库
* Matplotlib:绘图
安装方式:pip安装
    pip install matplotlib

* plotly：可交互绘图
安装方式：pip安装
    pip install matplotlib
# 常见的绘图类型
* 折线图
具体流程
- 导入相对应的库
- 格式化模块
- 得到x,y的数据
- style
- 美化图表
- 调用绘制方法
- 显示
示例
1. Matplotlib
    import Matplotlib.pyplot as plt

    x=
    y=
    fig,ax=

* 散点图
#导入相对应的库
#格式化模块
#得到x,y的数据
#style
* 美化图表
    - 
#调用绘制方法
#显示

* 平方图
* 饼状图

# 总结 一个绘图的简单流程
1. 导入相对应的库
2. 创造数据
3. 画图
4. 美化图表
5. 显示/存储

# API
1. 什么是API？
Wep API 是网站的一部分，用于与使用具体URl请求特定信息的程序交互。这种请求被称为API调用。
请求的数据将以易于处理的格式如JSON或CSV）返回。依赖于外部的数据源的大多数应用程序依赖于APi调用，如集成社交媒体网站的应用程序。
2. 具体调用APi
以调用Github的API 为例
#特定的URL发送请求即可
