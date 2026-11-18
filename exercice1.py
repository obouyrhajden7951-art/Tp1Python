class CompteurPage:

    # Attribut partagé entre toutes les pages
    total_visites = 0

    def __init__(self, nom_page):
        # Attributs propres à chaque page
        self.nom_page = nom_page
        self.visites = 0

        # Incrémenter le compteur global
        CompteurPage.total_visites += 1

    # Ajouter une visite à la page
    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visites += 1

    # Afficher les statistiques
    def afficher_statistiques(self):
        return f"Page '{self.nom_page}': {self.visites} visites. Total global: {CompteurPage.total_visites}"


# Création des objets
page1 = CompteurPage("Accueil")
page2 = CompteurPage("Contact")

# Ajouter des visites
page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

# Afficher les résultats
print(page1.afficher_statistiques())
print(page2.afficher_statistiques())
print(CompteurPage.total_visites)