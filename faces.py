# Prompt for user input and convert it with emoticons
def main():
    # Prompt for user input
    user_input = input("Enter a string: ")
    
    # Convert user input with emoticons
    user_input = convert_emoticons(user_input);
    
    # Display the converted string
    print(user_input)
    
def convert_emoticons(user_input):
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    return user_input

main()