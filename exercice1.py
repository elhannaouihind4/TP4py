
# Classe mère
class Animal:
    def parler(self):
        raise NotImplementedError(
            "Cette méthode doit être redéfinie"
        )


# Classe Chien
class Chien(Animal):
    def parler(self):
        return "Ouaf !"


# Classe Chat
class Chat(Animal):
    def parler(self):
        return "Miaou !"


#classe Vache
class Vache(Animal):
    def parler(self):
        return "Meuh !"


#classe Robot (duck typing)
class Robot:
    def parler(self):
        return "Bonjour ! Je suis un robot."


# Fonction commune
def faire_parler(animal):
    print(animal.parler())


# Programme principal
if __name__ == "__main__":

    #  collection d'objets différents
    animaux = [
        Chien(),
        Chat(),
        Chien(),
        Vache()
    ]

    print(" Polymorphisme avec les animaux ")

    for animal in animaux:
        faire_parler(animal)

    #  duck typing
    print("\n Duck typing avec le robot ")

    robot = Robot()
    faire_parler(robot)

    # Tous les objets dans une seule collection
    print("\n Collection mixte ")

    objets = [
        Chien(),
        Chat(),
        Vache(),
        Robot()
    ]

    for objet in objets:
        faire_parler(objet)
