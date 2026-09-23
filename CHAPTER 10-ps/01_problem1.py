# Create a class named Programmer
class Programmer:

    # Constructor to store programmer information
    def __init__(self, name, language, company):
        self.name = name
        self.language = language
        self.company = company


# Create objects for different programmers
programmer1 = Programmer("Rehan", "Python", "Microsoft")
programmer2 = Programmer("Rahul", "Java", "Microsoft")
programmer3 = Programmer("Aman", "C++", "Microsoft")


# Print programmer information
print(programmer1.name, programmer1.language, programmer1.company)
print(programmer2.name, programmer2.language, programmer2.company)
print(programmer3.name, programmer3.language, programmer3.company)