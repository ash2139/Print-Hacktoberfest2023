# Take user input for a string of characters
user_input = input("Enter a string of characters: ")

# Convert the input string to a list of characters
char_list = list(user_input)

# Sort the list of characters in alphabetical order
sorted_chars = sorted(char_list)

# Print the sorted characters
print("Characters in alphabetical order:", ''.join(sorted_chars))
