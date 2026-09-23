# Create a Calculator class
class Calculator:

    # Method to find square
    def square(self, number):
        return number * number

    # Method to find cube
    def cube(self, number):
        return number * number * number

    # Method to find square root
    def square_root(self, number):
        return number ** 0.5


# Create an object of Calculator
calc = Calculator()

# Call the methods
print("Square:", calc.square(5))
print("Cube:", calc.cube(5))
print("Square Root:", calc.square_root(25))