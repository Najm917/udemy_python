# A tuple in Python is an ordered, immutable collection used to store multiple items in a single variable. Tuples are defined using parentheses () (or comma-separated values).

# tupple:---Immutable (cannot change),, my_tuple = (1, 2),,Can be used as a key (hashable),, Fixed records, coordinates (x, y), RGB (r, g, b)

# list:--- Mutable (can append, pop, change),,my_list = [1, 2],,Cannot be used as a key (unhashable),, Dynamic collections where items change

point = (10, 20)
print(point[0])  # Output: 10

rgb = (255, 128, 0)
r, g, b = rgb

print(r)  # 255
print(g)  # 128
print(b)  # 0