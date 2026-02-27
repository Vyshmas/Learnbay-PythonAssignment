class flight:
   
   def __init__(self,flight_no,base_price,total_seat):
      self.flight_no=flight_no
      self.base_price=base_price
      self.total_seat=total_seat

   def display_flight_info(self):
      print(f"The Flight Deatils Are As Follows \n ----------------------------------")
      print(f"Filght No:{self.flight_no}\n Baseprice:{self.base_price} \n Totalseat: {self.total_seat}")

class domesticflight(flight):
     
     def __init__(self, flight_no, base_price, total_seat,tax_percent):
         super().__init__(flight_no, base_price, total_seat)
         self.tax_percent=tax_percent

     def calculate_price(self):
         self.Total_price=self.base_price+self.tax_percent
         print("Total Price of flight :",self.Total_price)
    
class bookingflight(domesticflight):
    def __init__(self, flight_no, base_price, total_seat, tax_percent,booked_seat):
        super().__init__(flight_no, base_price, total_seat, tax_percent)
        self.booked_seat=booked_seat

    def check_seat_avail(self):
        if self.total_seat <=0 :
            print("No seats are avaliable")
        else:
            print(f"There are {self.total_seat} avalible")
    
    def book_seat(self) :
       request_seat=self.total_seat-self.booked_seat
       print("Number of seat Booked:",self.booked_seat)
       print("Seat available After booking",request_seat)

    def get_finalprice(self):
        no_of_tickets = self.Total_price * self.booked_seat
        print("Total Number of tickets:",no_of_tickets)

p1=bookingflight("23DF890",10000,150,360.80,4)   
p1.display_flight_info()
p1.calculate_price()
p1.check_seat_avail()
p1.book_seat()
p1.get_finalprice()   