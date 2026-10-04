# import csv
import pandas

# with open("weather_data.csv") as data_file:
#   list_data=[]
#   data=csv.reader(data_file)
#   for row in data:
#     list_data.append(row)
#   print(list_data)
  
data =pandas.read_csv("weather_data.csv")
temp=data["temp"]
# ------------------------
# this is pythin syntex


# average=sum(temp)/len(temp)
# print(average)


# -----------------------
# pandas
print("get max:\n",data["temp"].max())
print("get average:\n",data.temp.mean())
# _____________________________________
# get data in columns
print("get columns:/n ",data.temp)
#           OR
print("get columns:\n",data["temp"])
# ________________________________________
# get data in row

print("get row:\n",data[data.day=="Monday"])
# _________________________________________
# average ,max,mean from data with day name  and all thinks

print("get max with day name:\n",data[data.temp==data.temp.max()])

# ______________________________________
# check specific data

monday=data[data.day=="Monday"]
print("check condition on monday:\n",monday.condition)

# check TEMP and convert into Fahrenheit
print("tem in C:\n",monday.temp)
print("temp in F:\n",(monday.temp*9/5)+32)

# ______________________________________
# dict to dataFrame

data_dict={
  "students":["Arif","Najm","Uddin"],
  "marks":[98,89,87]
}

data=pandas.DataFrame(data_dict)
data.to_csv("Data.csv")
print(data)