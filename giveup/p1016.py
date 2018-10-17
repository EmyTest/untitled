class Restaurent():
    def __init__(self,restaurent_name,cuisine_type):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(self.restaurent_name,":",self.cuisine_type)
    def open_restaurant(self):
        print("it is opening")

# restaurent = Restaurent("A","B")
# print("---",restaurent.restaurent_name," ",restaurent.cuisine_type)
# restaurent.describe_restuarant()
# restaurent.open_restaurant()

restraurant1 = Restaurent('A1','B1')
restraurant1.describe_restuarant()
restraurant2 = Restaurent('A2','B2')
restraurant2.describe_restuarant()
restraurant3 = Restaurent('A3','B3')
restraurant3.describe_restuarant()

