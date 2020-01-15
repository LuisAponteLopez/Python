def presentation():
    print("*"*100)
    print("This program orders the numbers that the user enters")
    print("*"*100)

def Enternumber(number):
    arrayNumber = []
    for i in range(number):
        number = eval(input("Enter the number "+str(i+1)+": "))
        arrayNumber.append(number)
    return arrayNumber

def bye():
    print("\n\nThanks for using the program, come back soon.")

def main():
    presentation()
    number = int(input("how much number are you going to enter? "))
    arrayNumber = Enternumber(number)
    arrayNumber.sort()
    print("\n")
    for i in arrayNumber:
        print(i,end=" ")
    
    bye()
main()
