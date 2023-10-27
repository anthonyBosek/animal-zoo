from lib.animal import Animal
from lib.zoo import Zoo

# code here


sd = Zoo(name="San Diego Zoo", location="San Diego, CA")

lion = Animal(species="Lion", weight=170, nickname="Cowardly", zoo=sd)
tiger = Animal(species="Tiger", weight=225, nickname="Tigger", zoo=sd)
bear = Animal(species="Bear", weight=368, nickname="Baloo", zoo=sd)


# ipdb allows us to stop our code & test stuff
import ipdb

ipdb.set_trace()
print("Thanks for visiting the zoo!")
