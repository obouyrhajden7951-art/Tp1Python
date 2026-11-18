class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    # @property : la méthode s'utilise comme un attribut (contact.initiale, sans parenthèses).
    # Elle est CALCULÉE à chaque accès, donc toujours à jour si le nom change.
    @property
    def initiale(self):
        """Retourne la première lettre du nom en majuscule."""
        # Expression conditionnelle : si le nom est vide, on évite l'erreur d'index
        return self.nom[0].upper() if self.nom else ""

    # __repr__ : représentation "technique" de l'objet, utilisée aussi dans les listes
    def __repr__(self):
        return f"Contact(nom='{self.nom}', email='{self.email}')"