class smartphone:
  purpose="communication and entertainment and internet  use"
  def __init__(self, brand, model, price):
    self.brand=brand
    self.model=model
    self.price=price
    
phone1=smartphone("apple","ipad","100k")
phone2=smartphone("nokia","3310","1000")
phone3=smartphone("samsung","s24","80k")
phone4=smartphone("realme","14pro","33k")

print(phone1.brand,phone1.model,phone1.price)

print(phone1.purpose)