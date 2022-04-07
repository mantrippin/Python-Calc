def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select Symbol.")
print("1.Add")
print("2.Subtract")
print("3.Multiply ")
print("4.Divide ")

while True:
    
    choice = input("Enter symbol choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second very cool number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        
        next_calculation = input("Do another operation?? (yes/no): ")
        if next_calculation == "no":
          print ("Made by manstrippin")
          break
    
    else:
     
        print("Invalid Input")