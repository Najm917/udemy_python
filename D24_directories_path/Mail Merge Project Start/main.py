PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    
    names=name_file.readlines()
    
    
with open("./Input/Letters/starting_letter.txt") as file:
    letter_content=file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt",mode="w") as complet_letter:
            complet_letter.write(new_letter)
        
        
    
    


    