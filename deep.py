# Prompt the user for the question
user_input = input("What is the answer to the Great Question of Life, the Universe and Everything:")
user_input = user_input.lower().strip()
if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
    print("Yes")
else:
    print("No")