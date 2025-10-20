print("Simple calculator")
i = 1

operation = ["1.Add","2.Minus","3.Multiple","4.Devision","5.End"]
while i == 1:
    try:
        number = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
    except ValueError:
        print("Please enter valid integers.")
        continue
    for x in operation:
        print(x)   
    try:
        selection = int(input("Please select operation: "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if selection == 1:
       print(number + number2)
    elif selection == 2:
       print(number - number2)
    elif selection == 3:
       print(number * number2)
    elif selection == 4:
       try:
           print(number / number2)
       except ZeroDivisionError:
           print("Error: division by zero is not allowed.")
    elif selection == 5:
       break
    else:
       print("Error, Please enter a correct option!")
