def full_name(f_name,l_name):
  # skip f/l_name
  if f_name=="" or l_name=="":
    return "you are skip name section please fill the name "
  
  f_name=f_name.title()
  l_name=l_name.title()
  return f"{f_name} {l_name}"

name=full_name(input("enter your f_name: "),input("enter your l_name: "))
print(name)