
def calculator():
    print("=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Average (/2)")
    print("7. Exponentiation (1st Number ^ 2nd Number)")

    choice = input("Choose an operation (1-7): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
    elif choice =="5":
        result = floor_divide(num1,num2)
    elif choice == "6":
        result = average(num1, num2)
    elif choice == "7":
        result = power (num1, num2)
    else:
        print("Invalid choice!")
        return

    print("Result:", result)

def power(a,b):
    return a**b

def multiply(a, b):
    return a * b

# Floor Division - Cescil (Member 5)
def floor_divide(a, b):
    return a // b if b != 0 else "Error: Cannot divide by zero!"

# Average - Claire (Member 6)
def average(a, b):
    return (a + b) / 2

calculator()

