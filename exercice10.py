import functools

# Créer un décorateur pour vérifier les valeurs positives
def valider_positif(*indices):

    def decorator(func):

        # Fonction qui vérifie les arguments
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            for idx in indices:
                if idx < len(args):
                    valeur = args[idx]

                    if not isinstance(valeur, (int, float)) or valeur <= 0:
                        raise ValueError(
                            f"L'argument à l'index {idx} doit être positif."
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorator


# Créer la classe Rectangle
class Rectangle:

    # Initialiser la largeur et la hauteur
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Calculer l'aire avec validation
    @valider_positif(1, 2)
    def aire(self, facteur=1.0):
        return self.largeur * self.hauteur * facteur


# Créer un rectangle
rect = Rectangle(5, 10)

# Calculer l'aire
print(rect.aire())

# Tester une valeur incorrecte
try:
    print(rect.aire(-1))
except ValueError as e:
    print(e)