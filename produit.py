from dataclasses import dataclass, field
from typing import List


# @dataclass génère automatiquement __init__, __repr__ et __eq__
# à partir des champs annotés ci-dessous.
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0          # valeur par défaut : champ facultatif à la création

    # Pour une valeur par défaut MUTABLE (liste, dict), il faut default_factory.
    # Écrire "tags: List[str] = []" est interdit : la même liste serait partagée
    # par tous les produits. default_factory crée une NOUVELLE liste à chaque objet.
    tags: List[str] = field(default_factory=list)

    def valeur_totale(self) -> float:
        return self.prix * self.quantite


# ===== TEST =====
p1 = Produit("Café", 5.5, 10, ["boisson", "chaud"])
p2 = Produit("Café", 5.5, 10, ["boisson", "chaud"])

print(p1)                  # Produit(nom='Café', prix=5.5, quantite=10, tags=['boisson', 'chaud'])
print(p1 == p2)            # True : __eq__ généré compare les valeurs des champs
print(p1.valeur_totale())  # 5.5 x 10 = 55.0

p3 = Produit("Thé", 3.0)   # quantite = 0 et tags = [] par défaut
print(p3.tags)             # []