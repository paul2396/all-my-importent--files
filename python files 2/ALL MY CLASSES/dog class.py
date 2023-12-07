class Dog:
    def __init__(self, name, group, appearance, temperament, special_skill=None):
        self.name = name
        self.group = group
        self.appearance = appearance
        self.temperament = temperament
        self.special_skill = special_skill

    def __str__(self):
        result = (
            f"name: {self.name}\n"
            f"group: {self.group}\n"
            f"Temperament: {self.temperament}\n"
        )
        if self.special_skill is not None:
            result += f"Special Skill: {self.special_skill}\n"
        return result

class LassDog(Dog):
    def __init__(self, name, group, appearance, temperament, special_skill):
        super().__init__(name, group, appearance, temperament)
        self.special_skill = special_skill

    def __str__(self):
        return super().__str__() + f"Special Skill: {self.special_skill}\n"

class Terrier(Dog):
    def __init__(self, name, appearance, temperament, special_skill=None):
        super().__init__(name, "Terrier", appearance, temperament, special_skill)

# Creating instances of the Terrier class
terrier1 = Terrier("Border Terrier", "Short wirey coat", "Friendly", "Great ratter")
terrier2 = Terrier("Sky Terrier", "Long silky coat", "Highly strung", 
                   "Not good with children")
terrier3 = Terrier("Jack Russell", "Principally white short smooth or broken coat", 
                   "Very intelligent", "Great ratter")
terrier4 = Terrier("Airedale Terrier", "Long shedding wiry coats", 
                   "Wonderful companions and family pets", "Excellent watchdogs")
terrier5 = Terrier("Bedlington Terrier","short curly coat",
                   "mild mannered affectionate","wonderful companions and family pets")
terrier6 = Terrier("Fox Terrier","Short wirey coat"," loyal affectionate and courageous","")

LassDog1 = LassDog("Labrador", "Gundog", "Golden or black", "Good-natured and dependable", 
                   "Good all-round gundog")
lassDog2 = LassDog("Bullmastiff", "Working", "Short smooth coat", "Good watchdogs", 
                   "Expensive to feed")
lassDog3=  LassDog("English Springer Spaniel", "Gundog", "Can be brown or black", 
                   "Reliable trustworthy", "Excellent gun dog")
lassDog4 = LassDog("English Setter","Gundog","long sleek coat"," loyal and affectionate by nature",
                   "in the right hands easy to train")
# Printing information about the terriers and LassDogs
print(terrier1)
print(terrier2)
print(terrier3)
print(terrier4)
print(lass_dog1)
print(lass_dog2)
print(lass_dog3)





          
        