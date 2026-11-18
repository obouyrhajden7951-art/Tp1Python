class JournalTaches:

    # Initialiser le nom du fichier
    def __init__(self, nom_fichier="journal.txt"):
        self.nom_fichier = nom_fichier
        self.fichier = None

    # Ouvrir le fichier au début du bloc with
    def __enter__(self):
        self.fichier = open(self.nom_fichier, "a", encoding="utf-8")
        return self

    # Fermer le fichier à la fin du bloc with
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichier:
            self.fichier.close()

        return False

    # Ajouter une tâche dans le fichier
    def ajouter_tache(self, description):
        if self.fichier:
            self.fichier.write(f"- {description}\n")
        else:
            raise RuntimeError("Le journal n'est pas ouvert.")


# Utiliser le gestionnaire de contexte
with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Réviser la POO")
    journal.ajouter_tache("Faire le TP 1")

# Lire le contenu du fichier
with open("taches_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())