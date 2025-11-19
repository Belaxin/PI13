from animal import animal
from dog import dog
from cat import cat


dog1 = dog("Dunco", 3)
cat1 = cat("Muro", 8)
entity1 = animal("Jano", 18)
dog2 = dog("Max", 14)

dog1.sound()
cat1.sound()
entity1.sound()

entity1.printAge()
entity1.ageUp()
entity1.printAge()