def display(result):
    if result == int(result):
        print("result:", int(result))
    else:
        print("result:", round(result, 2))


while True:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    operation = input("enter the operation(+,-,*,/): ")

    if operation == "+":
        display(num1 + num2)

    elif operation == "-":
        display(num1 - num2)

    elif operation == "*":
        display(num1 * num2)

    elif operation == "/":
        if num2 != 0:
            display(num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("invalid operation")

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "no":
        print("Calculator stopped")
        break

