number=100
while number>=1:
  
  if number%15==0:
    print("fifteen")
  elif number%3==0:
    print("three  ")
  elif number%5==0:
    print("five")
  else:
    print(number)
  number-=1  
  # This line is commented out, so the loop will run indefinitely
print("done")