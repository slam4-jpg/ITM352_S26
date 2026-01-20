def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract two numbers."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return x / y


def get_number(prompt, last_result=None):
    """Get a valid number input from the user."""
    while True:
        # Offer to use last result as first number
        if last_result is not None and "first" in prompt.lower():
            use_last = input(f"Use last result ({last_result}) as first number? (yes/no): ").strip().lower()
            if use_last in ['yes', 'y']:
                return last_result
        
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    """Get a valid operation choice from the user."""
    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide)
    }
    
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        choice = input("Enter choice (1/2/3/4): ").strip()
        
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    """Main function to run the calculator."""
    print("=" * 40)
    print("        Simple Calculator")
    print("=" * 40)
    
    last_result = None
    
    while True:
        try:
            # Get input numbers
            num1 = get_number("Enter first number: ", last_result)
            num2 = get_number("Enter second number: ")
            
            # Get operation
            operation_symbol, operation_func = get_operation()
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Display result
            print(f"\n{num1} {operation_symbol} {num2} = {result}")
            
            # Store result for next calculation
            last_result = result
            
        except ValueError as e:
            print(f"\n{e}")
        
        # Ask if user wants to perform another calculation
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nThank you for using the calculator. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()


