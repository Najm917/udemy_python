print("this is not actule calculator you need to choose by self number and sighn you want to perform")
def add (n1,n2):
  return n1+n2

def substract (n1,n2):
  return n1-n2

def multiply (n1,n2):
  return n1*n2


def devide (n1,n2):
  return n1/n2


operation={
  "+":add,
  "-":substract,
  "*":multiply,
  "/":devide
}
# sum=add(int(input("enter first number?: ")),int(input("enter second num?: ")))
number=float(input("Enter a first number: "))
calculator=True
while calculator:

  for symbol in operation:
    print(symbol)
  # sight=input("+\n-\n*\n/\n pick an operation?: ")
  sighn=input("pick an operation?:")
  number2=float(input("enter a second number?: "))
  
  # if sighn=="+":
  #   print(f"{number} {sighn} {number2} = {add(number,number2)}")
  # elif sighn=="-":
  #   print(f"{number} {sighn} {number2} = {substract(number,number2)}")
  # elif sighn=="*":
  #   print(f"{number} {sighn} {number2} = {multiply(number,number2)}")
  # elif sighn=="/":
  #   print(f"{number} {sighn} {number2} = {devide(number,number2)}")
  # else:
  #   print(f"you choose wront sighn please select {sighn} choose any of these: ")
  
  answer=operation[sighn](number,number2)
  print(f"{number} {sighn} {number2} = {answer}")
  continues=input(f"Want have an opration you perform?: y {answer} and  n or new calculation: ").strip().upper()
  if continues=="Y":
    number=answer
    continue
  else:
    calculator=False
    exit()
  
  
    
    