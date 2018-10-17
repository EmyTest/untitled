# class Restaurent():
#     def __init__(self,restaurent_name,cuisine_type):
#         self.restaurent_name = restaurent_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restuarant(self):
#         print(self.restaurent_name,":",self.cuisine_type)
#     def open_restaurant(self):
#         print("it is opening")
#
# # restaurent = Restaurent("A","B")
# # print("---",restaurent.restaurent_name," ",restaurent.cuisine_type)
# # restaurent.describe_restuarant()
# # restaurent.open_restaurant()
#
# restraurant1 = Restaurent('A1','B1')
# restraurant1.describe_restuarant()
# restraurant2 = Restaurent('A2','B2')
# restraurant2.describe_restuarant()
# restraurant3 = Restaurent('A3','B3')
# restraurant3.describe_restuarant()

# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_name(self):
#         print("first_name:",self.first_name,"last_name:",self.last_name)
#     def greet_user(self):
#         print("hello",self.first_name," ",self.last_name)
#
# user1 = User('Alice','Tom')
# user1.describe_name()
# user1.greet_user()
# user2 = User("Mary",'Bob')
# user2.describe_name()
# user2.greet_user()
# user3 = User("Tony",'Belbert')
# user3.describe_name()
# user3.greet_user()



# class Restraurant():
#     def __init__(self,restraurant_name,cuisine_type):
#         self.restaurant_name = restraurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name,":",self.cuisine_type)
#
#     def open_restaurant(self):
#         print("is opening")
#
#     def set_number_served(self,number):
#         self.number_served = number
#
#     def get_number_served(self):
#         return self.number_served
#
#     def increment_number_served(self,number):
#         while self.number_served < number:
#             print(self.number_served)
#             self.number_served += 1
#
# restraurant = Restraurant('A','B')
# print(restraurant.restaurant_name," ",restraurant.cuisine_type)
# restraurant.describe_restaurant()
# restraurant.open_restaurant()
# print(restraurant.get_number_served())
# restraurant.set_number_served(2)
# print(restraurant.get_number_served())
# restraurant.increment_number_served(10)


# class User():
#     """docstring for User"""
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_name(self):
#         print("fitst_name :", self.first_name, " last_name: ", self.last_name)
#
#     def greet_user(self):
#         print("hello, ", self.first_name, " ", self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# user1 = User('Alice','Tom')
# user1.describe_name()
# print("login_attempts:",user1.login_attempts)
# user1.increment_login_attempts()
# print("login_attempts:",user1.login_attempts)
# user1.increment_login_attempts()
# print("login_attempts:",user1.login_attempts)
# user1.reset_login_attempts()
# print("login_attempts:",user1.login_attempts)


# class Restraurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.restaurant_name,":",self.cuisine_type)
#
#     def open_restaurant(self):
#         print("is opening")
#
#     def set_number_served(self,number):
#         self.number_served = number
#
#     def get_number_served(self):
#         return self.number_served
#
#     def increment_number_served(self,number):
#         while self.number_served < number:
#             print(self.number_served)
#             self.number_served += 1
#
# class IceCreamStand(Restraurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['banaa','apple','orange']
#     def show_icecram(self):
#         for s in self.flavors:
#             print(s)
#
#
# icecream = IceCreamStand('Hang','Big')
# icecream.show_icecram()
# icecream.describe_restaurant()
#


'''super关键字'''
# class Parent(object):
#     def __init__(self,name):
#         self.name = name
#         print("create an instance of :",self.__class__.__name__)
#         print("name attribute is:",self.name)
# #定义子类child 继承父类parent
# class Child(Parent):
#     def __init__(self):
#         print("call __init__ from child class")
#         super(Child,self).__init__("data from child")
# # c = Child()
# # print(c.name)
# d = Parent('tom')
# c = Child()
# print(c.name)

# class Parent(object):
#     Value = "hi ,parent value"
#     def fun(self):
#         print("this is from Parent")
# class child(Parent):
#     Value = "hi,child value"
#     def ffun(self):
#         print("this is from child")
# c = child()
# c.fun()
# c.ffun()
# print(child.Value)
#
#
# class Parent(object):
#     Value = "Hi, Parent value"
#     def fun(self):
#         print("This is from Parent")
#
# class Child(Parent):
#     Value = "Hi, Child  value"
#     def fun(self):
#         print("This is from Child")
#         Parent.fun(self)   #调用父类Parent的fun函数方法
#
# c = Child()
# c.fun()

# class User():
#     """docstring for User"""
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_name(self):
#         print("fitst_name :", self.first_name, " last_name: ", self.last_name)
#
#     def greet_user(self):
#         print("hello, ", self.first_name, " ", self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Admin(User):
#     """docstring for Admin"""
#
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = ['can add post', 'can ban user', 'can delete post']
#
#     def show_privileges(self):
#         print(self.privileges)
#
#
# admin = Admin("Alice", 'Bob')
# admin.show_privileges()
#


# class User():
#     """docstring for User"""
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_name(self):
#         print("fitst_name :", self.first_name, " last_name: ", self.last_name)
#
#     def greet_user(self):
#         print("hello, ", self.first_name, " ", self.last_name)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Privileges():
#     """docstring for Privileges"""
#
#     def __init__(self):
#         self.privileges = ['can add post', 'can ban user', 'can delete post']
#
#     def show_privileges(self):
#         print(self.privileges)
#
#
# class Admin(User):
#     """docstring for Admin"""
#
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()
#
#     def show_privileges(self):
#         self.privileges.show_privileges()
#
#
# admin = Admin("Alice", 'Bob')
# admin.show_privileges()


# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' '+ self.model
#         return long_name
#     def read_odometer(self):
#         print("this car has" + str(self.odometer_reading) + "miles on it.")
#
#     def updata_odometer(self,milegeage):
#         if milegeage >= self.odometer_reading:
#             self.odometer_reading = milegeage
#         else:
#             print("you can not roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
#
# class Battery():
#     def __init__(self,battery_size=70):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print("this car has a "+str(self.battery_size) + "-kWh battery")
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = "this car go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#         self.upgrade_battery()
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery_size = Battery()
#
#     def describe_battery(self):
#         self.battery_size.battery_size()
#     def get_range(self):
#         self.battery_size.get_range()
#
# my_tesla = ElectricCar('tesla','model s',2016)
# my_tesla.get_range()
# my_tesla.get_range()
#

