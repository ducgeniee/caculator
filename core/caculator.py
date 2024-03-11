from plugins import Base


class Application:
    def __init__(self):
        # Load all plugins into application dynamically
        self.plugins = Base.plugins

    def add(self, x, y):
        return x + y

    def perform_operation(self, operation, x, y):
        operations = [plugin.operation_name() for plugin in self.plugins]
        if operation in operations:
            index = operations.index(operation)
            return self.plugins[index].execute(x, y)
        else:
            raise ValueError(f"No plugin found for operation '{operation}'")

    def run(self):
        print("Welcome to the Simple Calculator App!")
        while True:
            print("\nSelect an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Exit")

            choice = input("Enter your choice (1, 2, 3, or 4): ")

            if choice in ['1', '2', '3']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = 0
                if choice == '1':
                    result = self.add(num1, num2)
                elif choice == '2':
                    operation = 'subtraction'
                    result = self.perform_operation(operation, num1, num2)
                elif choice == '3':
                    operation = 'multiplication'
                    result = self.perform_operation(operation, num1, num2)
                print("Result:", result)
            elif choice == '4':
                print("Thank you for using the Simple Calculator App!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
