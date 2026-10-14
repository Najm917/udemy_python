file = None
try:
    file = open("a_file.txt")
    a_dict = {"key": "val"}
    print(a_dict["jjjhjjjhbhb"])
except FileNotFoundError:
    # Triggered if the file is missing
    with open("a_file.txt", "w") as file:
        file.write("uijhjghgjhg")
    print("File was missing, so a new one was created.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    if file and not file.closed:
        file.close()
        print("file was closed")