import requests
from plotly.graph_objs import Bar
from plotly import offline


url=r'https://api.github.com/seatch/respositories?q=language:python&sort=stars'#调用API
headers={'Accept':'application/vnd.github.v3+json'}#
response=requests.get(url,headers=headers,verify=False)#关闭ssl证书验证
print(response.status_code)

#处理结果
r=response.json()

#探索有关仓库的信息
repo_dicts=r['items']
repo_name,stars=[],[]
print(len(repo_dicts))
for repo_dict in repo_dicts:
    repo_name.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
data=[{
    'type':'bar',
    'x':'repo_names',
    'y':'stars',
}]
my_layout={
    'title':'github上最受欢迎的python项目',
    'xaxis':{'title':'repositort'},
    'yaxix':{'title':'stars',}
}

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
