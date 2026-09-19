num = input("Enter a number: ")
print(f"Multiplication Table for {num}:")
try:
    int(num)
    a=[3,5]
    print(a[num])
 #   for i in range(1, 11):        
   #     print(f"{num} × {i} = {num * i}")
except ValueError:
    print("Invalid input! Please enter a valid integer  ")
except Exception as e:
    print(f"valid input{e}")
print("there ia no error")