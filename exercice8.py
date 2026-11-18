class Vecteur2D:

    # Initialiser les coordonnées du vecteur
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Additionner deux vecteurs
    def __add__(self, autre):
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    # Soustraire deux vecteurs
    def __sub__(self, autre):
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    # Multiplier le vecteur par un nombre
    def __mul__(self, scalaire):
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    # Comparer deux vecteurs
    def __eq__(self, autre):
        if not isinstance(autre, Vecteur2D):
            return False

        return self.x == autre.x and self.y == autre.y

    # Afficher le vecteur
    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"


# Créer deux vecteurs
v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)

# Effectuer les opérations
v3 = v1 + v2
print(v3)

v4 = v2 - v1
print(v4)

v5 = v1 * 2
print(v5)

# Comparer deux vecteurs
print(v1 == Vecteur2D(1, 2))