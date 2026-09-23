class employee:
    language = "py"
    salary = 1200000  #This is a class attribute

    def getinfo(self):
        print("The language is{self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

        
rehan = employee
rehan.greet()
rehan.getinfo()