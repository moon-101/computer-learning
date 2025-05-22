"""
#5.1作业
cat='lion'
print("Is cat=='lion'? I predict True")
print(cat=='lion')
dog='tianyuan'
print("Is dog=='tianyuan' I predict True")
print(dog=='tianyuan')
print(dog=="cat")
"""
"""
#5.2
a='asdf'
b='zxcv'
c='asdf'
print('false')
print(a==b)
print('true')
print(a==c)
"""
"""
a='ASDF'
b='asdf'
print('true')
print(b.upper())
print(a==b.upper())
"""
"""
a=5
b=3
c=5
list_1=[3,1]
print(a!=b)
print(a==b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a>b and b > a)
print(a>b or b>a)
print(a in list_1)
print(b not in list_1)
"""
#5.3
"""
alien_color="green"
if alien_color=="green":
    print("你得到五分")"""
"""
alien_color="red"
if alien_color=='green':
    print('gg')
#5.4
alien_color="green"
if alien_color=="red":
    print("get 5")
else:
    print("get 10")

#5.5
alien_color="red"
if alien_color=="green":
    print("5")
elif alien_color=="yellow":
    print("10")
else:
    print("15")
"""
"""
#5.6
age=int(input())
if age<2:
    print("baby")
elif 2<=age<4:
    print("da baby")
elif 4<=age<13:
    print("child")
elif age==13 or age<20:
    print("teenager")
elif age==20 or age<65:
    print("adult")
elif age>=65:
    print("old man")

#5.7
favorite_furits=['apple','banana','tomato']
if 'apple' in favorite_furits:
    print("You really like apple")

"""
"""
#5.8
list_1=['1','2','3','4','5','admin']
if list_1==[]:
    print("we")
else:
    for name in list_1:
        if name == "admin":
            print(f"{name}hello")
        else:
            print("hello")
del list_1[0:]
print(list_1)

#5.9
#5.10

current_users=["1",'2','3','4','5']
new_users=['1','2','a','s','d']

for name in new_users:
    x=current_users[:]
    for i in x:
        x.append(i.lower())
        x.pop(0)
    if name.lower() in x:
        print("需要输入别的用户名")
    else:
        print("未被使用")
    """
#5.11
list_2=['1','2','3','4','5','6','7','8','9']
for i in list_2:
    if i=='1':
        print('\n1st')
    elif i=='2':
        print('\n2nd')
    elif i=='3':
        print('3rd')
    else:
        print(f"{i}th")

