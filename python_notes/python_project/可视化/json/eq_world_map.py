import plotly.express as px
import json
import pathlib
import webbrowser

# 设置输出路径
output_path = pathlib.Path(r"D:\games\computer-learning\python_notes\python_project\可视化\output")
output_path.mkdir(exist_ok=True)

# 加载数据
filename = r'D:\games\computer-learning\python_notes\python_project\可视化\data\eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

# 处理数据
all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    props = eq_dict['properties']
    geom = eq_dict['geometry']
    mags.append(props['mag'])
    titles.append(props['title'])
    # 注意：GeoJSON 格式是 [经度, 纬度, 高度]
    lons.append(geom['coordinates'][0])
    lats.append(geom['coordinates'][1])

# 创建地理散点图 - 使用 scatter_geo 替代 scatter
fig = px.scatter_geo(
    lat=lats,  # 纬度
    lon=lons,  # 经度
    labels={"lon": "经度", "lat": "纬度"},
    scope='world',  # 显示全球地图
    width=1200,     # 增加宽度以更好地显示全球地图
    height=800,
    title="全球地震分布图",
    hover_name=titles,
    size=[m if m > 0 else 0.1 for m in mags],  # 根据震级设置点的大小
    color=mags,         # 根据震级着色
    color_continuous_scale='Viridis',
    projection='natural earth',  # 使用自然地球投影
    opacity=0.7,       # 设置透明度
)

# 更新地图布局
fig.update_geos(
    showcountries=True,  # 显示国家边界
    showcoastlines=True,  # 显示海岸线
    coastlinecolor="Gray",
    showland=True,       # 显示陆地
    landcolor="LightGreen",
    showocean=True,      # 显示海洋
    oceancolor="LightBlue",
)

# 更新图例和颜色条
fig.update_layout(
    coloraxis_colorbar=dict(
        title="震级",
        thickness=15,
        len=0.75,
    ),
    margin=dict(l=0, r=0, t=50, b=0),  # 减少边距
)

# 保存并显示
html_file = output_path / "global_earthquakes.html"
fig.write_html(html_file)

# 直接打开HTML文件
webbrowser.open('file://' + str(html_file))

# 尝试在浏览器中显示
try:
    fig.show(renderer="browser")
except:
    print("无法在浏览器中显示，请直接打开HTML文件")