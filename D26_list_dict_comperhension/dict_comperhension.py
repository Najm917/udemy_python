import random
import pandas 
data=["arif","najm","uddin"]
new_data={
  students:random.randint(50,90) for students in data
}

# print(new_data)

passed_students={student:score for (student,score) in new_data.items() if score>=56}
# print(passed_students)

# __________________________________
new_dict_students={
  "students":["najm","arif","uddin"],
  "marks":[56,78,90]
}
new_data1=pandas.DataFrame(new_dict_students)
for (key,val) in new_data1.items():
  print(val)
  # ______________________________
  
  for (index,row) in new_data1.iterrows():
    print(row) 