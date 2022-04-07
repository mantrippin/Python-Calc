def add(x, y):
    return x + y
# This is for adding

def subtract(x, y):
    return x - y
#Subtracting

def multiply(x, y):
    return x * y
#Multiplying

def divide(x, y):
    return x / y
#And dividing

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
#Entering the number is here
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
# Adding
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
# Subtracting
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
# Multiplying
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        # Dividing
        
        
        next_calculation = input("Do another operation?? (yes/no): ")
        if next_calculation == "no":
          print ("Made by manstrippin")
          break
    
    else:
     # By the way, I didn't fully make this on my own I had to search up a few things for help
        print("Invalid Input")
      