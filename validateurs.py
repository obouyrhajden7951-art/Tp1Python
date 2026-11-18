import functools


# Un décorateur AVEC arguments s'écrit en 3 niveaux imbriqués :
# 1) valider_positif(*indices)  : reçoit les paramètres du décorateur
# 2) decorator(func)            : reçoit la fonction à décorer
# 3) wrapper(*args, **kwargs)   : remplace la fonction, s'exécute à chaque appel
def valider_positif(*indices: int):
    """Décorateur qui valide que les arguments aux indices donnés sont positifs."""
    def decorator(func):
        # functools.wraps conserve le nom et la docstring de la fonction d'origine
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # *args = tous les arguments positionnels, rassemblés dans un tuple.
            # Pour une méthode, args[0] est self.
            for idx in indices:
                # On ne contrôle que si l'argument a réellement été fourni
                if idx < len(args):
                    value = args[idx]
                    if not isinstance(value, (int, float)) or value <= 0:
                        raise ValueError(f"L'argument à l'index {idx} doit être un nombre positif.")
            # Tout est valide : on appelle la vraie fonction
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ===== APPLICATION À UNE CLASSE =====
class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        self.largeur = largeur
        self.hauteur = hauteur

    # Indices contrôlés : 1 et 2. Mais les arguments de aire() sont seulement
    # (self, facteur) : l'index 1 est "facteur" et l'index 2 n'existe pas (voir remarque).
    @valider_positif(1, 2)
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur


# ===== TEST =====
rect = Rectangle(5, 10)
print(rect.aire())          # 50.0 (aucun argument fourni : rien à valider)

try:
    rect.aire(-1)           # facteur = -1 : refusé par le décorateur
except ValueError as e:
    print(e)                # L'argument à l'index 1 doit être un nombre positif.