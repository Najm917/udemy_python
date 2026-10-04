import pandas

data=pandas.read_csv("central park.csv")
gray_color=len(data[data["Primary Fur Color"]=="Gray"])
print(f"torat gyar color:{gray_color}")

White_color=len(data[data["Primary Fur Color"]=="White"])
print(f"torat white color:{White_color}")

Red_color=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(f"torat Cinnamon color:{Cinnamon_color}")
print(type(Cinnamon_color))

black_color=len(data[data["Primary Fur Color"]=="Black"])
print(f"torat black color:{black_color}")

data_dist={
  "four color":["Black","Red","Gray","White"],
  "Count":[gray_color,Red_color,White_color,black_color]
}

dataframe=pandas.DataFrame(data_dist)
dataframe.to_csv("squirral_count.csv")