class Restaurent():
    def __init__(self,restaurent_name,cuisine_type):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(self.restaurent_name,":",self.cuisine_type)
    def open_restaurant(self):
        print("it is opening")

restaurent = Restaurent("A","B")
print("---",restaurent.restaurent_name," ",restaurent.cuisine_type)
restaurent.describe_restuarant()
restaurent.open_restaurant()



