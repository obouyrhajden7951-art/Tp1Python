class Article:
    # Les annotations (: str, : float) sont des "type hints" : elles documentent
    # et aident l'IDE, mais Python ne les impose pas à l'exécution.
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Calcule la valeur totale du stock en HT."""
        # Méthode "pure" : elle calcule et renvoie une valeur sans modifier l'objet
        return self.prix_ht * self.stock

    def ajouter_stock(self, quantite: int):
        """Ajoute une quantité au stock actuel."""
        # Validation AVANT de modifier l'état : l'objet reste toujours cohérent
        if quantite < 0:
            raise ValueError("La quantité ajoutée ne peut pas être négative.")
        self.stock += quantite

    # __str__ : appelée par print(objet) et str(objet), pour un affichage lisible
    def __str__(self):
        # :.2f = 2 décimales
        return f"[{self.reference}] {self.designation} - Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}€"


# ===== TEST =====
a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)
print(a1.valeur_stock())   # 89.99 x 10 = environ 899.9
a1.ajouter_stock(5)        # stock : 10 + 5 = 15
print(a1)                  # [REF-001] Clavier Mécanique - Stock: 15 - Prix HT: 89.99€