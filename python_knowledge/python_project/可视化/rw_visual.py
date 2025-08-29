import plotly.graph_objects as go
from random_walk import RandomWalk

while True:
    # 创建带默认参数的实例
    rw = RandomWalk(num_points=5000)  # 明确指定点数
    
    try:
        rw.fill_walk()
    except ValueError as e:
        print(f"数据生成错误: {str(e)}")
        break

    # 创建图表对象
    fig = go.Figure()
    
    # 添加轨迹（优化括号结构）
    scatter = go.Scatter(
        x=rw.x_values,
        y=rw.y_values, 
        mode='markers+lines',
        marker=dict(
            size=4,
            color=list(range(len(rw.x_values))),
            colorscale='Viridis',
            showscale=True,
            line=dict(width=0.5, color='DarkSlateGrey')
        )
    )
    fig.add_trace(scatter)
    
    # 布局配置
    fig.update_layout(
        title=dict(
            text='专业随机漫步可视化',
            x=0.5,
            font=dict(size=24)
        ),
        height=600
    )
    
    # 显示图表
    fig.show()
    fig.write_html("test_plot.html")  # 确保能生成文件
    
    # 用户交互（添加容错处理）
    while True:
        keep = input('继续生成？(y/n)\n').lower()
        if keep in ('y', 'n'):
            break
        print("请输入 y 或 n")
    
    if keep == 'n':
        break
