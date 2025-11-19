import datetime

class Person:
    # Konstruktor
    def __init__(self, name: str,surName: str, year: int):
        self.name = name
        self.surName = surName
        self.year = year
    
    def greet(self):
        print(f"Ahojky ja som {self.name} {self.surName}.")

    def declareAge(self):
        print(f"{self.name}: Som {(datetime.date.today().year - int(self.year))} rokov stary.")