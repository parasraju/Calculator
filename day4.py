import math

def calculator():
    history = []
    while True:
        print("\nSimple Calculator")
        print("Operations: +, -, *, /, %, **, //, sqrt, fact, sin, cos, tan, log, convert, exit")
        op = input("Enter operation: ").lower()
        
        if op == "exit":
            print("Goodbye!")
            break
        elif op in {"sqrt", "fact", "sin", "cos", "tan", "log"}:
            num = float(input("Enter a number: "))
            if op == "sqrt": result = math.sqrt(num)
            elif op == "fact": result = math.factorial(int(num))
            elif op == "sin": result = math.sin(math.radians(num))
            elif op == "cos": result = math.cos(math.radians(num))
            elif op == "tan": result = math.tan(math.radians(num))
            elif op == "log": result = math.log(num)
        elif op == "convert":
            print("1: Temperature (C to F)", "2: Length (m to km)", "3: Weight (kg to lbs)", sep="\n")
            choice = input("Enter conversion type: ")
            value = float(input("Enter value: "))
            if choice == "1": result = (value * 9/5) + 32
            elif choice == "2": result = value / 1000
            elif choice == "3": result = value * 2.20462
            else: print("Invalid choice"); continue
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if op == "+": result = num1 + num2
            elif op == "-": result = num1 - num2
            elif op == "*": result = num1 * num2
            elif op == "/": result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif op == "%": result = num1 % num2
            elif op == "**": result = num1 ** num2
            elif op == "//": result = num1 // num2
            else: print("Invalid operation"); continue
        
        print("Result:", result)
        history.append(f"{op} {num1 if 'num1' in locals() else ''} {num2 if 'num2' in locals() else ''} = {result}")
        
        if input("View history? (y/n): ").lower() == "y":
            print("\n".join(history))

calculator()
