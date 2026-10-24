class Vecteur2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        """Surcharge de l'opérateur +"""
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        """Surcharge de l'opérateur -"""
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire: float) -> 'Vecteur2D':
        """Surcharge de l'opérateur * (multiplication par un scalaire)"""
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    def __eq__(self, autre: object) -> bool:
        """Surcharge de l'opérateur =="""
        if not isinstance(autre, Vecteur2D):
            return False
        return self.x == autre.x and self.y == autre.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"


v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)

print(v1 + v2)
print(v2 - v1)
print(v1 * 2)
print(v1 == Vecteur2D(1, 2))