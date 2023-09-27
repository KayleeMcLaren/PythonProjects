PLACEHOLDER = "[name]"  # Used to represent the name of the person who is receiving the letter


with open("./Input/Names/invited_names.txt") as names_file:  # Opens the file ./Input/Names/invited_names.txt and assigns it to the variable names_file
    names = names_file.readlines()  # Reads all of the lines in the file and returns them as a list. The list of names is then assigned to the variable names

with open("./Input/Letters/starting_letter.txt") as letter_file:  # Opens the file ./Input/Letters/starting_letter.txt and assigns it to the variable letter_file
    letter_contents = letter_file.read()  # Reads the entire contents of the file and returns it as a string. The contents of the letter are then assigned to the variable letter_contents
    # Iterates over the list of names and creates a new letter for each name
    for name in names:
        stripped_name = name.strip()  # strip() method is used to remove any leading or trailing whitespace from the name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # replace() method is used to replace the PLACEHOLDER placeholder with the name of the person who is receiving the letter. The new letter is assigned to the variable new_letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:  # opens a new file called f"./Output/ReadyToSend/letter_for_{stripped_name}.txt" and assigns it to the variable completed_letter
            completed_letter.write(new_letter)  # write() method is then used to write the new letter to the file
