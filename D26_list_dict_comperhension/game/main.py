import pandas as pd

# Load CSV
word = pd.read_csv("words.csv")

# 1. Match your exact CSV column names (e.g. Letter, Word)
phonetic_dict = {row.Letter: row.Word for (index, row) in word.iterrows()}


user_input = input("Enter your name:\n").strip().upper()

# 3. List comprehension looking up each character
result = [phonetic_dict[letter] for letter in user_input ]

print(result)

# letter_map = dict(zip(word["Letter"].str.upper(), word["Word"]))

# user_input=input("enter  your name:\n")

# result = [
#     f"{char.upper()}: {letter_map[char.upper()]}"
#     for char in user_input
#     if char.upper() in letter_map
# ]

# for item in result:
#   print(item)