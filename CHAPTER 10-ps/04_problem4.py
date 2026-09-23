# Create a Calculator class
class Calculator:

    # Static method
    @staticmethod
    def greet():
        print("Hello, welcome to Calculator!")

    # Method to find square
    def square(self, number):
        return number * number

    # Method to find cube
    def cube(self, number):
        return number * number * number

    # Method to find square root
    def square_root(self, number):
        return number ** 0.5


# Create an object
calc = Calculator()

# Call static method
calc.greet()

# Call calculator methods
print("Square:", calc.square(5))
print("Cube:", calc.cube(5))
print("Square Root:", calc.square_root(25))