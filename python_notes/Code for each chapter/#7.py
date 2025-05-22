"""
#7.1
car=input('you need car?')
print(f"I can find {car}")
#7.2
kehu=int(input('duoshaorenyongchang?'))
if kehu > 8:
    print("meiweizhile")
else:
    print("haiyouweizhi")
#7.3
number=int(input("shu"))
if number % 10==0:
    print(f"{number}keyibeizhenchu")
else:
    print(f"{number}bunengbeizhenchu")
"""
"""
#7.4
biaozhi=True
while biaozhi:
    pizza=input("peizhi")
    if pizza=='quiz':
        biaozhi=False
#7.5
biaozhi=True
while biaozhi:
    age=input("age")
    if age=="quiz":
        break
    elif int(age)<3:
        print("free")
    elif 3<=int(age)<=12:
        print("10")
    elif int(age)>12:
        print("15")

        
        """
"""
#7.6
age=input('age')
while age!='quiz':
    if int(age)<3:
        print('free')
    elif 3<=int(age)<=12:
        print("10")
    elif int(age)>12:
        print("15")
    age=input('age')
"""
#7.7
"""
age=True
x=1
while age:
    x+=1
    print(x)
"""
#7.8
sandwich_orders=["1",'2','34','5']
finished_orders=[]
while sandwich_orders:
    i=sandwich_orders.pop(0)
    print(f'I made your tuna {i}')
    finished_orders.append(i)
print(finished_orders)
#7.9
sandwich_orders=['pastrami','pastrami','pastrami','pastrami','pastrami']
while sandwich_orders:
    sandwich_orders.pop(0)
if 'pastrami' not in sandwich_orders:
    print("sdoushanchule")
#7.10
active=True
while active:
    x=input("where you go?")
    print(x)

