discount=10
def product_details(prod_id,prod_name,prod_price):
    discount
    total_price=prod_price - (prod_price*discount/100)
    print("the prodcut details")
    print("------------------------")
    print("product_id",prod_id)
    print("product_Name",prod_name)
    print("total_price",total_price)

    def final_price(quantity,price):
      discount
      finalprice=quantity*price
      discount_price= finalprice-(finalprice*discount/100)
      return discount_price
    
    prd_total= final_price(10,1000)
    print("the final price after discount:",prd_total)
product_details("1001","books",1000)