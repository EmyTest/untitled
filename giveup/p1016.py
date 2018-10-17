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


class Restraurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name,":",self.cuisine_type)

    def open_restaurant(self):
        print("is opening")

    def set_number_served(self,number):
        self.number_served = number

    def get_number_served(self):
        return self.number_served

    def increment_number_served(self,number):
        while self.number_served < number:
            print(self.number_served)
            self.number_served += 1

class IceCreamStand(Restraurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['banaa','apple','orange']
    def show_icecram(self):
        for s in self.flavors:
            print(s)


icecream = IceCreamStand('Hang','Big')
icecream.show_icecram()
icecream.describe_restaurant()

