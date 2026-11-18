class Carnet:

    # Créer une liste vide de contacts
    def __init__(self):
        self.contacts = []

    # Ajouter un contact
    def ajouter(self, contact):
        self.contacts.append(contact)

    # Rechercher un contact par son nom
    def chercher(self, nom_partiel):
        nom_partiel = nom_partiel.lower()

        return [c for c in self.contacts
                if nom_partiel in c.nom.lower()]

    # Retourner le nombre de contacts
    def __len__(self):
        return len(self.contacts)


# Créer le carnet
carnet = Carnet()

# Créer deux contacts
c1 = Contact("Alice Dupont", "0612345678", "alice@example.com")
c2 = Contact("Bob Martin", "0698765432", "bob@example.com")

# Ajouter les contacts
carnet.ajouter(c1)
carnet.ajouter(c2)

# Afficher l'initiale
print(c1.initiale)

# Rechercher un contact
resultats = carnet.chercher("ali")
print(resultats)

# Afficher le nombre de contacts
print(len(carnet))