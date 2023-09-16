import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Gets user input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# Randomly gets the letters and adds them to the password_list array
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Randomly gets the symbols and adds them to the password_list array
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# Randomly gets the numbers and adds them to the password_list array
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# Shuffles the array to put the values in a random order
random.shuffle(password_list)

# Takes the values from the array and stores them as a string
password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
