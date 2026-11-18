import math


class Cercle:
    def __init__(self, rayon: float):
        # Attention : "self.rayon = ..." n'écrit pas directement un attribut,
        # cela appelle le SETTER défini plus bas. La validation s'applique donc
        # dès la création : Cercle(-3) échoue tout de suite.
        self.rayon = rayon

    # GETTER : s'exécute quand on LIT c.rayon
    @property
    def rayon(self):
        """Accès au rayon."""
        return self._rayon   # la vraie valeur est stockée dans _rayon

    # SETTER : s'exécute quand on ÉCRIT c.rayon = valeur
    # Le nom après @ doit être identique à celui de la propriété (rayon.setter)
    @rayon.setter
    def rayon(self, valeur: float):
        """Contrôle de la valeur du rayon."""
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        # Le préfixe _ signale un attribut interne : on ne l'utilise pas depuis l'extérieur
        self._rayon = valeur

    def aire(self) -> float:
        return math.pi * self.rayon ** 2      # pi x r au carré

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon       # 2 x pi x r

    def __str__(self):
        return f"Cercle(rayon={self.rayon})"


# ===== TEST =====
c = Cercle(5.0)
print(c.aire())            # 78.53981633974483

try:
    c.rayon = -10          # déclenche le setter, qui lève ValueError
except ValueError as e:
    print(f"Erreur interceptée : {e}")   # Le rayon doit être strictement positif.