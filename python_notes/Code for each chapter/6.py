
"""
#6.1
man={'last_name':'feng',
     'first_name':'li',
     'age':'18',
     'city':'beijing',
     }
print(man)

#6.2
like_number={'lihua':'1',
             'bixia':'2',
             'maozhedong':'3',
             'libai':'4',
             'wocao':'5'
             }
print(like_number)
"""
"""
#6.3
chihuibiao={'变量':'带有指向性的量，如字符串或数字',
            '列表':'一列具有特定顺序的元素组成的集合',
            '元组':'无法改变顺序的列表',
            '字典':'由键值对组成的',
            'if语句':'条件判断是否执行语句',
            'for循环':'有限循环',
            '键':'字典的相关概念',
            '值':'字典的相关概念',
            'print()':'输出函数',
            'input()':'输入函数',
            'format()':'插入',
            'title()':'标题函数',
            }
print('一些编程概念解释：')
for i in chihuibiao:
    n=chihuibiao[i]
    print(f'\n{i}')
    print(f'\n{n}')

#6.4
"""

"""#6.5
helius={'黄河':'中国',
       '长江':'秦朝',
       '鸭绿江':'东北',
       }
for key,value in helius.items():
    print(f'{key} through {value}')
for key in helius.keys():
    print(key)
for value in helius.values():
    print(value)
"""
"""
#6.6
names={}
list_1=['a','b','c','d','f','g']
for name in list_1:
    if name in names.keys():
        print(f'thank you{name}')
    else:
        print(f'invate{name}')
"""
"""
#6.7
xiaoming={'first_name':'xiao',
          'last_name':'ming',
          'xinbie':'zhishenji',
          }
yingdang={'first_name':'ying',
          'last_name':'dang',
          'xinbe':'gouwudai',
          }
people=[xiaoming,yingdang]
for man in people:
    print(man)
#6.8
nike={'animal':'dog',
      'zhuren':'xiaohong',
      }
peter={'animal':'cat',
       'zhuren':'xiaohuang',
       }
pets=[nike,peter]
for pet in pets:
    print(pet)
#6.9
favorite_places={"xiaoming":['beijing','xian','xingjiang']
                 "xiaohong":"shanghai",
                 "xiaohua":"guandong",
                 }
"""
"""
#6.10
like_numbers={'maozhedong':['1'],
              'libiao':'101',
              'zhude':'2',
              'pendhuai':'401',
              }
for key,value in like_numbers.items():
    print(key)
    print(value)
    print('\n')
"""
#6.11
cities={
    'beijing':{
        '国家':'china',
        'renkou':'2000wang',
        },
    'shanghai':{
        '国家':'qing',
        'population':'1000wang',
        'fact':'sea',
        } # type: ignore
    }
for key, value in cities.items():
    print(key)
    for K,V in value.items():
        print(K)
        print(V)