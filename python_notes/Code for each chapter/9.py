#9.1
""""""

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} opening")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,number_new):
        self.number_served+=number_new
   

kendeiji=Restaurant('bejingfandian','chinacai')
print(kendeiji.number_served)
kendeiji.set_number_served(10)
print(kendeiji.number_served)
kendeiji.increment_number_served(100)
print(kendeiji.number_served)
kendeiji.describe_restaurant()

kendeiji.open_restaurant()
maidanlao=Restaurant('fenkuanxinqishi','kuaichan')
maidanlao.describe_restaurant()
xiancai=Restaurant('xiangcai','difancai')
xiancai.describe_restaurant()


class User:
    def __init__(self,first_name,last_name,aihao,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.aihao=aihao
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.aihao}")
    
    def greet_user(self):
        self.first_name=self.first_name.title()
        self.last_name=self.last_name.title()
        print(f"Hello {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

"""
"""
lee=User("sijian","lee","game",9)
lee.describe_user()
lee.greet_user()
for i in range(10):
    lee.increment_login_attempts()
    print(lee.login_attempts)
lee.reset_login_attempt()
print(lee.login_attempts)

#9。6
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['apple','banana','piano']
    
    def menu(self):
        print(self.flavors)

kuchao=IceCreamStand('kuchao','suiguodian')
kuchao.menu()

#9.7
"""
class admin(User):
    def __init__(self,first_name,last_name,aihao,login_attempts):
        super().__init__(first_name,last_name,aihao,login_attempts)
        self.privileges=['leeshen','zhaodao','zhunong']
    
    def show_privileges(self):
        print(self.privileges)

admin_1=admin('linmu','lin','yao','101')
admin_1.show_privileges()
"""

#9.8
class Privileges:
    def __init__(self):
        self.privileges=['jieshi','xiaozhang','liya']
    
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,aihao,login_attempts):
        super().__init__(first_name,last_name,aihao,login_attempts)
        self.privilege=Privileges()

admin=Admin('sijian','lee','bianchen','101')
admin.privilege.show_privileges()
"""
#9.9
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size !=100 :
            self.battery_size=100
    
    def get_range(self):
        
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        
        elif self.battery_size == 100:
            range = 315
        
        print(f"{range}")


BYD=Battery()
BYD.upgrade_battery()
BYD.get_range()

#9.10
"""
 

        