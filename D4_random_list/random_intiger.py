import random

# randint return int valve give range 
# a=random.randint(1,10)
# print(a)

# random return floating poin number between 0 to 1

floating_number=random.random()*10
# print(floating_number)

# uniform return floting point number given range

float_num=random.uniform(0,10)
# print(floating_number)

random_head_tail=random.randint(0,1)
if random_head_tail==0:
  print("Heads")
else:
  print("Tails")