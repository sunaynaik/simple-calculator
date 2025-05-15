from utils.operations import *
import os

def menu():
    print("\n--- Scientific Calculator ---")
    print("1. Basic Operation (+, -, *, /)")
    print("2. Scientific Operation (sin, cos, log, sqrt, pow, factorial)")
    print("3. View Memory")
    print("4. Exit")

def save_to_memory(expression, result):
    with open("data/memory.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                op = input("Enter operator (+, -, *, /): ")

                result = basic_operations(a, b, op)
                print(f"Result: {result}")
                save_to_memory(f"{a} {op} {b}", result)

            elif choice == '2':
                func = input("Enter function (sin, cos, log, sqrt, pow, factorial): ").lower()

                if func in ['sin', 'cos', 'log', 'sqrt', 'factorial']:
                    num = float(input("Enter number: "))
                    result = scientific_operation(func, num)
                    print(f"Result: {result}")
                    save_to_memory(f"{func}({num})", result)

                elif func == 'pow':
                    base = float(input("Enter base: "))
                    exp = float(input("Enter exponent: "))
                    result = scientific_operation(func, base, exp)
                    print(f"Result: {result}")
                    save_to_memory(f"pow({base}, {exp})", result)

                else:
                    print("Invalid function")

            elif choice == '3':
                if os.path.exists("data/memory.txt"):
                    with open("data/memory.txt", "r") as file:
                        print("\n--- Memory ---")
                        print(file.read())
                else:
                    print("No memory saved yet.")

            elif choice == '4':
                print("Exiting Calculator. Goodbye!")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
