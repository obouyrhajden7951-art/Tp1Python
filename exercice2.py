class Article:

    # Initialiser les attributs de l'article
    def __init__(self, reference, designation, prix_ht, stock):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    # Calculer la valeur totale du stock
    def valeur_stock(self):
        return self.prix_ht * self.stock

    # Ajouter une quantité au stock
    def ajouter_stock(self, quantite):
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative.")

        self.stock += quantite

    # Afficher les informations de l'article
    def __str__(self):
        return f"[{self.reference}] {self.designation} - Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}€"


# Créer un article
a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)

# Afficher la valeur du stock
print(a1.valeur_stock())

# Ajouter 5 articles
a1.ajouter_stock(5)

# Afficher l'article
print(a1)