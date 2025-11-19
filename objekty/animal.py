class animal:
    def __init__(self, name: str, age: int):
        if not isinstance(age, int):
            raise TypeError("age must be an int")
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} made a sound.")

    def ageUp(self):
        self.age = self.age+1

    def printAge(self):
        print(f"{self.name} ma {self.age} rokov")