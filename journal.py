class JournalTaches:
    def __init__(self, nom_fichier: str = "journal.txt"):
        self.nom_fichier = nom_fichier
        self.fichier = None          # le fichier n'est pas encore ouvert

    # __enter__ s'exécute à l'entrée du bloc "with".
    # Sa valeur de retour est ce que reçoit la variable après "as".
    def __enter__(self):
        # Mode 'a' = append : on ajoute à la fin sans écraser le contenu existant
        self.fichier = open(self.nom_fichier, 'a', encoding='utf-8')
        return self

    # __exit__ s'exécute TOUJOURS à la sortie du bloc, avec ou sans erreur.
    # exc_type, exc_val, exc_tb décrivent l'exception éventuelle (None sinon).
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichier:
            self.fichier.close()
        # False : on ne "mange" pas l'exception, elle continue de se propager
        return False

    def ajouter_tache(self, description: str):
        """Ajoute une tâche au journal."""
        if self.fichier:
            self.fichier.write(f"- {description}\n")   # \n = retour à la ligne
        else:
            # Appeler cette méthode hors d'un bloc with est une erreur de programmation
            raise RuntimeError("Le journal n'est pas ouvert. Utilisez 'with'.")


# ===== TEST =====
with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Réviser la POO")
    journal.ajouter_tache("Faire le TP 1")
# ici __exit__ a été appelé : le fichier est fermé

# Relecture du fichier pour vérifier (encodage précisé pour les accents)
with open("taches_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())