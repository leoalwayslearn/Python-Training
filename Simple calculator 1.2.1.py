#Generating a simple calculator
#Version 1.2.1
#Improvements:Simple the code structure, add a exit optionafter calculation
i = 1
operation = ["1.Add","2.Minus","3.Multiple","4.Devision"]
print("Welcome to simple calculator V1.2.1")
#Run the loop
while i == 1:
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
    except ValueError:
        print("Plese type a number!")
        continue
    for x in operation:
        print(x)
    try:
        selection = int(input("Plese select operation:"))
    except ValueError:
        print("Plese select a valid option!")
        continue
    if selection == 1:
        print("The result is %d"%(num1 + num2))
    elif selection ==2:
        print("The result is %d"%(num1 - num2))
    elif selection == 3:
        print("Teh result is %d"%(num1* num2))
    elif selection == 4:
        if num2 == 0:
            print("Undefined(cannot devide by zero)!")
        else:
            print("The reslut is %.2f"%(num1/num2))
    else:
        print("Error, plese select a valid option!")
        continue
    repeat = input("Do you want to perform another calculation? (y/n):")
    if repeat=='y':
        print ("Thanks for using the porgramme!")
        break
    else:
        continue
#End of the programm
    

