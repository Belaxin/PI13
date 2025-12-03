from Person import Person
from Ucitel import Ucitel
from Student import Student
import random

triedaRad = ["I", "II", "III", "IV"]
triedaPis = ["A", "B", "C", "D"]
titul = ["Mgr.", "Ing.", "PaeDr."]
predmet = ["Matematika", "Slovencina", "Fyizika"]
rok = [2009, 2008, 2007, 2006]
studenti = []
ucitelia = []

mena = open("objektyHodina\mena.txt", 'r', encoding="utf8")
menaList = [line.strip() for line in mena.readlines()]
priezviska = open("objektyHodina\priezviska.txt", 'r', encoding="utf8")
priezviskaList = [line.strip() for line in priezviska.readlines()]



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


for i in range(10):
    trieda = random.randint(0,3)
    studenti.append(Student(menaList[random.randint(0,len(menaList)-1)], priezviskaList[random.randint(0,len(priezviskaList)-1)], rok[trieda], str(f"{triedaRad[trieda]}.{triedaPis[random.randint(0,3)]}")))
    ucitelia.append(Ucitel(menaList[random.randint(0,len(menaList)-1)], priezviskaList[random.randint(0,len(priezviskaList)-1)], random.randint(1950, 2000),titul[random.randint(0,2)], predmet[random.randint(0,2)] ,str(f"{triedaRad[random.randint(0,3)]}.{triedaPis[random.randint(0,3)]}")))
print("\n\n\n")
for i in ucitelia:
    print(i)
print("\n\n\n")
for i in studenti:
    print(i)