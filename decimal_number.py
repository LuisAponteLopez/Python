
print("*"*60)
print("This program return the decimal par of a number")
print("*"*60)
number = input("Enter a number: ")
point = number.count(".")
if point == 0:
      print(".00") 
else:
    number = number.split(".")
    print(number[1])
print("Thanks for using program, come back soon")
