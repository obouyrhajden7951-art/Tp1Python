class Convertisseur:

    # Taux de conversion
    taux_eur_dh = 10.9

    # Méthode statique pour convertir les euros en dirhams
    @staticmethod
    def vers_dh(euros):
        return euros * Convertisseur.taux_eur_dh

    # Méthode de classe pour modifier le taux
    @classmethod
    def changer_taux(cls, nouveau_taux):
        if nouveau_taux <= 0:
            raise ValueError("Le taux doit être positif.")

        cls.taux_eur_dh = nouveau_taux

    # Convertir les dirhams en euros
    @classmethod
    def depuis_dh(cls, dirhams):
        return dirhams / cls.taux_eur_dh


# Convertir 100 euros en dirhams
print(Convertisseur.vers_dh(100))

# Changer le taux de conversion
Convertisseur.changer_taux(11.0)

# Convertir 110 dirhams en euros
print(Convertisseur.depuis_dh(110))

# Créer un objet
conv = Convertisseur()
print(conv.vers_dh(50))