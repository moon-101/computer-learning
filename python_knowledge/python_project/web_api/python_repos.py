import requests

url=r'https://api.github.com/seatch/respositories?q=language:python&sort=stars'#调用API
headers={'Accept':'application/vnd.github.v3+json'}#
response=requests.get(url,headers=headers,verify=False)#关闭ssl证书验证
print(response.status_code)
r=response.json()
print(r.keys())
print(r['total_count'])

#探索有关仓库的信息
repo_dicts=r['items']
print(len(repo_dicts))
for repo_dict in repo_dicts:
    print(repo_dict['name'])
    

#研究第一个仓库
repo_dict=repo_dicts[0]

print(len(repo_dict))#查询该仓库有多少键值对
for key in sorted(repo_dict.keys()):#打印这个仓库的所有键
    print(key)
print(repo_dict['name'])


#研究有关仓库的信息

