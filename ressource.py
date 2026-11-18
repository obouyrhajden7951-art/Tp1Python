class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        print(f"[INIT] Création de la ressource '{nom}'")

    # __del__ est appelée quand Python détruit l'objet (plus aucune référence vers lui).
    # Le moment exact n'est PAS garanti : à utiliser avec précaution.
    def __del__(self):
        """Appelé quand l'objet est détruit."""
        print(f"[DEL] Destruction de la ressource '{self.nom}'")

    def utiliser(self):
        print(f"[USE] Utilisation de '{self.nom}'")


# ===== TEST =====
import gc   # module du ramasse-miettes (garbage collector)

r = Ressource("Fichier de données")
r.utiliser()

# "del r" supprime la VARIABLE r. L'objet est détruit si plus rien ne le référence.
del r

# Force un passage du ramasse-miettes. Avec CPython, l'objet est déjà détruit
# dès le "del r" (comptage de références), mais cette ligne rend le comportement
# sûr même dans les cas où des références circulaires existent.
gc.collect()