class employee:
    language = "py"
    salary = 1200000  #This is a class attribute

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print("The language is{self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

        
rehan = employee("Rehan", 1300000, "javascript")
print(rehan.name, rehan.salary, rehan.language)