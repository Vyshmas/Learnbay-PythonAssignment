class product:
   
   def __init__(self,name,price,brand,warranty):
       self.name=name
       self.price=price
       self.brand=brand
       self.warranty=warranty

   def display(self):
        print(f"the product details are as follow:\n Name:{self.name} \n Price:{self.price} \n Brand:{self.brand} \n Warranty:{self.warranty} \n ----------------------------")

   def cal_price(self):
        total=self.price*self.count
        print("The total price:",total)

class electronics(product):
    type="electronics"
    count= 10

    def displayalldetails(self):
         print(f"the product  Complete details are as follow:\n Name:{self.name} \n Price:{self.price} \n Brand:{self.brand} \n Warranty:{self.warranty} \n type:{self.type} \n count: {self.count}")


mobile=electronics("mobile",1000,"samsung","3 years")
mobile.display()
mobile.displayalldetails()
mobile.cal_price()