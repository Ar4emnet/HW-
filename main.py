try:
    # task 1
    message = input("write message: ")
    count_letter = 0
    count_number = 0
    for letter in message:
        if letter.isalpha():
            count_letter += 1
        elif letter.isdigit():
            count_number += 1
    print(f"A letter in a message = {count_letter}, a number in a message = {count_number}")
    # task 2
    message = input("write message: ")
    symbol = input("Specify a character to search for: ")
    count_symbol = 0
    for letter in message:
        if letter == symbol:
            count_symbol += 1
    print(f"The following characters were found = {count_symbol}")
    # task 3
    message = input("write message: ")
    word1 = input("which word should be replaced: ")
    word2 = input("What word to replace it with: ")
    message = message.replace(word1, word2)
    print(f"new message: {message}")
except Exception as error:
    print(f"\tException occurred: {error}")

