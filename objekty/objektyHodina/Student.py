from Person import Person

class Student(Person):
    def __init__(self, name, surName, year, trieda: str):
        super().__init__(name, surName, year)
        self.trieda = trieda
    
    def greet(self):
        print(f"Ahojky ja som {self.name} {self.surName} z triedy {self.trieda}.")

    def __str__(self):
        return super().__str__()