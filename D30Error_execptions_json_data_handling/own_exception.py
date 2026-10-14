height=eval(input("enter tour height in inch:\n"))
weidth=eval(input("enter tour weidth in inch:\n"))
if height>120:
  raise TypeError("humen height is not longer then 150 inch")
bmi=weidth/height**2
print(bmi)