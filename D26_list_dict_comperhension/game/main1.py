
import pandas
word=pandas.read_csv("words.csv")

letter_map = dict(zip(word["Letter"].str.upper(), word["Word"]))

user_input=input("enter  your name:\n")

result = [
    f"{char.upper()}: {letter_map[char.upper()]}"
    for char in user_input
    if char.upper() in letter_map
]

for item in result:
  print(item)