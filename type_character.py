print("*"*100)
print("This program determine if a character entered is letter, number, or neither. (It only works with one character). If it is a letter, determine if it is uppercase or lowercase.")
print("*"*100)


character = input("Enter a character: ")
character = ord(character)
if 65 <= character and character <=90:
    print("It's a capital letter.")
elif 97<= character and character<= 122:
    print("It's a lower case letter.")

elif 48 <= character and character <= 57:
    print("It's a number")
else:
    print("It is not letter or number.")
print("Thanks for using the program, come back soon")
