import gc

class Ressource:

    # Initialiser la ressource
    def __init__(self, nom):
        self.nom = nom
        print(f"[INIT] Création de la ressource '{nom}'")

    # Méthode appelée lors de la destruction
    def __del__(self):
        print(f"[DEL] Destruction de la ressource '{self.nom}'")

    # Utiliser la ressource
    def utiliser(self):
        print(f"[USE] Utilisation de '{self.nom}'")


# Créer un objet
r = Ressource("Fichier de données")

# Utiliser l'objet
r.utiliser()

# Supprimer l'objet
del r

# Lancer le ramasse-miettes
gc.collect()