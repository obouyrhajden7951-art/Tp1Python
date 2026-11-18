class CompteurPage:
    # ATTRIBUT DE CLASSE : défini dans la classe, hors de toute méthode.
    # Il n'existe qu'en UN seul exemplaire, partagé par tous les objets.
    total_visites = 0

    def __init__(self, nom_page):
        # ATTRIBUTS D'INSTANCE : définis avec self.
        # Chaque objet a les siens : page1.visites et page2.visites sont indépendants.
        self.nom_page = nom_page
        self.visites = 0
        # On passe par le nom de la classe pour modifier l'attribut PARTAGÉ.
        # Écrire self.total_visites += 1 créerait un attribut d'instance qui masquerait
        # celui de la classe : c'est un piège classique.
        CompteurPage.total_visites += 1

    def ajouter_visite(self):
        self.visites += 1                  # compteur propre à cette page
        CompteurPage.total_visites += 1    # compteur global

    def afficher_statistiques(self):
        return f"Page '{self.nom_page}': {self.visites} visites. Total global: {CompteurPage.total_visites}"


# ===== TEST =====
page1 = CompteurPage("Accueil")   # total_visites passe à 1
page2 = CompteurPage("Contact")   # total_visites passe à 2

page1.ajouter_visite()            # total 3
page1.ajouter_visite()            # total 4
page2.ajouter_visite()            # total 5

print(page1.afficher_statistiques())  # Page 'Accueil': 2 visites. Total global: 5
print(page2.afficher_statistiques())  # Page 'Contact': 1 visites. Total global: 5
print(CompteurPage.total_visites)     # 5