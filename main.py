try:
    message = input("write message: ")
    count_letter = 0
    count_number = 0
    for letter in message:
        if letter.isalpha():
            count_letter += 1
        elif letter.isdigit():
            count_number += 1
    print(f"A letter in a message = {count_letter}, a number in a message = {count_number}")
except Exception as error:
    print(f"\tException occurred: {error}")