import math

class Cercle:

    # Initialiser le cercle avec son rayon
    def __init__(self, rayon):
        self.rayon = rayon

    # Lire la valeur du rayon
    @property
    def rayon(self):
        return self._rayon

    # Modifier le rayon avec une vérification
    @rayon.setter
    def rayon(self, valeur):
        if valeur <= 0:
            raise ValueError("Le rayon doit être positif.")

        self._rayon = valeur

    # Calculer l'aire du cercle
    def aire(self):
        return math.pi * self.rayon ** 2

    # Calculer le périmètre du cercle
    def perimetre(self):
        return 2 * math.pi * self.rayon

    # Afficher le cercle
    def __str__(self):
        return f"Cercle(rayon={self.rayon})"


# Créer un cercle
c = Cercle(5.0)

# Afficher l'aire
print(c.aire())

# Tester une valeur incorrecte
try:
    c.rayon = -10
except ValueError as e:
    print("Erreur :", e)