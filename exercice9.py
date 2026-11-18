from dataclasses import dataclass, field
from typing import List

# Définir une classe de données
@dataclass
class Produit:

    # Définir les attributs
    nom: str
    prix: float
    quantite: int = 0
    tags: List[str] = field(default_factory=list)

    # Calculer la valeur totale
    def valeur_totale(self):
        return self.prix * self.quantite


# Créer deux produits
p1 = Produit("Café", 5.5, 10, ["boisson", "chaud"])
p2 = Produit("Café", 5.5, 10, ["boisson", "chaud"])

# Afficher les informations
print(p1)

# Comparer les produits
print(p1 == p2)

# Afficher la valeur totale
print(p1.valeur_totale())

# Créer un produit avec les valeurs par défaut
p3 = Produit("Thé", 3.0)
print(p3.tags)