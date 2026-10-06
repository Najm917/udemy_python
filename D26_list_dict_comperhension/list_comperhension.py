number=[1,2,3,4]
# new_list=[]
# for n in number:
#   add=n+1
#   new_list.append(add)
  
# print(new_list)
# ____________________________
# list comperhension
new_list=[n+1 for n in number]

# print(new_list)

name="arif"
lette_list=[letter*2 for letter in range(10)]

# print(lette_list)

# _______________________________
names=["arif","najmuddin","john","amit kumar"]
# create a new list when have 4 and less letter

new_name=[name.upper() for name in names if len(name)<5]
print(new_name)