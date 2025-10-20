print("Simple calculator")
number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
operation = ["1.Add","2.Minus","3.Multiple","4.Devision"]
for x in operation:
    print(x)
selection=int(input("Plese select operation: "))
if(selection == 1):
    add = number + number2
    print(add)
elif(selection == 2):
    minus = number - number2
    print(minus)
elif(selection == 3):
    multiple = number * number2
    print(multiple)
elif(selection == 4):
    division = number / number2
    print(float(division))
else:
    print("Error, Plese run again!")
    

