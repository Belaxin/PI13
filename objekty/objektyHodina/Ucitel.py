from Person import Person
import datetime

class Ucitel(Person):
    def __init__(self, name: str, surName: str, year: int, title: str, subject: str, classs= ""):
        super().__init__(name, surName, year)  # inheritancia konstruktora
        self.subject = subject
        self.title = title
        self.classs = classs

    def greet(self):
        print(f"Ahojky ja som {self.title}{self.name} {self.surName}, ucim {self.subject} a som triedny ucitel triedy {self.classs}")

    def __str__(self):
        return(f"{self.title} {self.name} {self.surName} {(datetime.date.today().year - int(self.year))} - Ucitel, Predmet: {self.subject}, Trieda: {self.classs}")