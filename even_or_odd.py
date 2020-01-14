print("*"*100)
print("This program tells us if the number is even or odd.")
print("*"*100)

num  = int(input("Enter a integer: "))
number = num % 2
if number == 0:
    print(num,"is even")
else:
    print(num,"is odd")
print("thanks for using the program,come back soon,")
