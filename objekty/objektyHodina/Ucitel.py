from Person import Person

class Ucitel(Person):
    def __init__(self, name: str, surName: str, year: int, title: str, subject: str, classs= ""):
        super().__init__(name, surName, year)  # inheritancia konstruktora
        self.subject = subject
        self.title = title
        self.classs = classs

    def greet(self):
        print(f"Ahojky ja som {self.title}{self.name} {self.surName}, ucim {self.subject} a som triedny ucitel triedy {self.classs}")