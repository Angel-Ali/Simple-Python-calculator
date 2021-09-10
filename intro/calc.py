#imports
from display import print_menu, print_header


#global vars



#direct intructions
print_header()
print_menu()

option = input("Select an Option: ")

num1 = float(input("Please provide num1: "))
num2 = float(input("Please provide num2: "))

if option == "1":
    res = num1 + num2
  

elif option == "2":
    res = num1 - num2

elif option == "3":
    res = num1 * num2

elif option == "4":
    if num2 == 0:
        print("Error: Zero division is not allwed")
    res = "Error"

    
    print(f"The Result is: {res}")