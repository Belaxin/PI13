from Person import Person
from Ucitel import Ucitel
from Student import Student
import random

triedaRad = ["I", "II", "III", "IV"]
triedaPis = ["A", "B", "C", "D"]
titul = ["Mgr.", "Ing.", "PaeDr."]
predmet = ["Matematika", "Slovencina", "Fyzika"]
rok = [2009, 2008, 2007, 2006]
studenti = []
ucitelia = []
triedy = []
for i in range(4):
    for j in range(4):
        triedy.append(str(f"{triedaRad[i]}.{triedaPis[j]}"))

with open("objektyHodina\mena.txt", 'r', encoding="utf8") as mena:
    menaList = [line.strip() for line in mena.readlines()]
with open("objektyHodina\priezviska.txt", 'r', encoding="utf8") as priezviska:
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

for i in range(len(triedy)):
    ucitelia.append(Ucitel(random.choice(menaList), random.choice(priezviskaList), random.randint(1950, 2000),random.choice(titul), random.choice(predmet), triedy[i]))

for i in range(10):
    trieda = random.randint(0,3)
    ucitelia.append(Ucitel(random.choice(menaList), random.choice(priezviskaList), random.randint(1950, 2000),random.choice(titul), random.choice(predmet)))
    
for i in range(30):
    trieda = random.randint(0,3)
    studenti.append(Student(random.choice(menaList), random.choice(priezviskaList), rok[trieda], str(f"{triedaRad[trieda]}.{random.choice(triedaPis)}")))
    

random.shuffle(ucitelia)


print("\n\n\n")
for i in ucitelia:
    print(i)
print("\n\n\n")
for i in studenti:
    print(i)
    i.greet()