print("*"*100)
print("This program tells you if the year is leap or not.")
print("*"*100)
year = int(input("Enter a year: "))
year4=year%4
if year4 == 0:
    year100= year%100
    if year100 == 0:
        year400 = year%400
        if year400 == 0:
            print(year,"is leap")
        else:
            print(year,"is no leap")
    else:
        print(year,"is leap")
else:
    print(year,"is no leap")
print("Thaks for using the program,come back soon")
    
