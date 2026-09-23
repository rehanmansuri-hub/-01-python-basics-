# Create a class
class Student:

    # We can use 'slf' instead of 'self'
    def __init__(slf, name):
        slf.name = name

    # We can also use 'harry'
    def show(harry):
        print("Name:", harry.name)


# Create object
student = Student("Rehan")

# Call method
student.show()