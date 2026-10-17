def calculator():
    print("=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (1st Number ^ 2nd Number)")

    choice = input("Choose an operation (1-5): ")

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
    elif choice == "5":
        result = power (num1, num2)
    else:
        print("Invalid choice!")
        return

    print("Result:", result)

def power(a,b):
    return a**b

calculator()


