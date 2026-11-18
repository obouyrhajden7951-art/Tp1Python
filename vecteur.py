class Vecteur2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Les méthodes "dunder" (double underscore) sont appelées automatiquement
    # par Python quand on utilise l'opérateur correspondant.

    # v1 + v2  devient  v1.__add__(v2)
    # Les guillemets autour de 'Vecteur2D' sont nécessaires : la classe n'est pas
    # encore entièrement définie au moment où l'annotation est lue.
    def __add__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        """Surcharge de l'opérateur +"""
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    # v1 - v2  devient  v1.__sub__(v2)
    def __sub__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        """Surcharge de l'opérateur -"""
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    # v1 * 2  devient  v1.__mul__(2)   (le scalaire doit être à DROITE)
    def __mul__(self, scalaire: float) -> 'Vecteur2D':
        """Surcharge de l'opérateur * (multiplication par un scalaire)"""
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    # v1 == v2  devient  v1.__eq__(v2) : égalité par valeur
    def __eq__(self, autre: object) -> bool:
        """Surcharge de l'opérateur =="""
        # Si l'autre objet n'est pas un Vecteur2D, il ne peut pas être égal
        if not isinstance(autre, Vecteur2D):
            return False
        return self.x == autre.x and self.y == autre.y

    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"


# ===== TEST =====
v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)

print(v1 + v2)                  # Vecteur2D(4, 6)
print(v2 - v1)                  # Vecteur2D(2, 2)
print(v1 * 2)                   # Vecteur2D(2, 4)
print(v1 == Vecteur2D(1, 2))    # True : deux objets différents mais mêmes valeurs