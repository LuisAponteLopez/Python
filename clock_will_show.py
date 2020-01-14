x="*"
print(x*100)
print("This program defines the future time. Alone is allowed in the 12 hour and whole number format.")
print(x*100)

currentTime = eval(input("Enter the current time: "))
amountOfTime = eval(input("Enter the amount of time: "))
sumCandaA= currentTime + amountOfTime

while sumCandaA > 12:
     sumCandaA-=12
    
    
print('In',amountOfTime,'hours, the clock will show',sumCandaA)
print('Thanks for using the program, come back soon.')
