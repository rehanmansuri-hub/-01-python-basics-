# Create a class
class Demo:

    # Class attribute
    a = 10


# Create an object
obj = Demo()

# Print class attribute
print("Before:", obj.a)

# Set 'a' directly using the object
obj.a = 0

# Print object attribute
print("Object a:", obj.a)

# Print class attribute using class name
print("Class a:", Demo.a)