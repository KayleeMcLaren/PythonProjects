import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")  # Reads the CSV file nato_phonetic_alphabet.csv into a Pandas DataFrame and assigns it to the variable data
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Creates a dictionary from the DataFrame, where the keys are the letters of the alphabet and the values are the NATO phonetic alphabet codes for the letters. The iterrows() method iterates over the rows of the DataFrame, and the index variable contains the index of the current row. The row variable contains the current row as a Pandas Series

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]  # Creates a list of the NATO phonetic alphabet codes for the letters in the word. The for loop iterates over the letters in the word, and the phonetic_dict[letter] expression returns the NATO phonetic alphabet code for the current letter.
print(output_list)


# Example output:

# Enter a word: hello
# ['HOTEL', 'ECHO', 'LIMA', 'LIMA', 'OSCAR']
