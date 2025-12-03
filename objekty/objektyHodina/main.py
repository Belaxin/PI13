from Person import Person
from Ucitel import Ucitel
from Student import Student

ucitel1 = Ucitel("Michal", "Choma", 2001, "Mgr.", "Fyzika", "1.AT")
student1 = Student("Koppy", "Israelit", 2007, "3.AT")
person1 = Person("Jano", "Bucaneer", 1860)

ucitel1.greet()
ucitel1.declareAge()
student1.greet()
student1.declareAge()

print(student1) 

print(ucitel1)
person1.greet()
person1.declareAge()