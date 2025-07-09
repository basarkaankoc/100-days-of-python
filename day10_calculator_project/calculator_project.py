import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def substract(n1,n2):
    return n1 - n2

operations = {"+": add,
              "*": multiply,
              "/": divide,
              "-": substract,
}


def calculator():
    num1 = float(input("What's the first  number?: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        choose_operation = input("Pick an operation:"  )
        num2 = float(input("What's the next number?:"))

        result = operations[choose_operation](num1,num2)
        print(f"{num1} {choose_operation} {num2} = {result}")

        choice = input("Type 'y' to continue calculating with the result, 'n' to start a new calculation, or 'c' to exit: ").lower()

        if choice == "y":
            num1 = result

        elif choice == "n":
            should_continue = False
            print("\n "* 25)
            calculator()
        elif choice == "c":
            should_continue = False
            print("Calculator exited. Goodbye!")

        else:
            should_continue = False
            print("Invalid input. Please choose 'y', 'n', or 'c'.")

calculator()