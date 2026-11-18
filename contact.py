class Contact:

    # Initialiser les informations du contact
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    # Retourner la première lettre du nom
    @property
    def initiale(self):
        if self.nom:
            return self.nom[0].upper()
        return ""

    # Afficher les informations du contact
    def __repr__(self):
        return f"Contact(nom='{self.nom}', email='{self.email}')"