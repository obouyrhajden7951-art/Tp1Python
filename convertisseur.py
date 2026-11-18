class Convertisseur:
    # Attribut de classe : taux EUR -> DH, partagé et modifiable pour toute la classe
    taux_eur_dh = 10.9

    # @staticmethod : ne reçoit NI self NI cls. C'est une simple fonction rangée
    # dans la classe parce qu'elle est liée au sujet. Elle n'utilise que ses arguments
    # (et ici la classe, par son nom).
    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit des euros en dirhams (méthode statique)."""
        return euros * Convertisseur.taux_eur_dh

    # @classmethod : reçoit la CLASSE en premier argument (cls), pas l'instance.
    # Elle peut donc lire ou modifier les attributs de classe.
    @classmethod
    def changer_taux(cls, nouveau_taux: float):
        """Modifie le taux de change (méthode de classe)."""
        if nouveau_taux <= 0:
            raise ValueError("Le taux doit être positif.")
        cls.taux_eur_dh = nouveau_taux     # modifie la valeur pour tout le monde

    @classmethod
    def depuis_dh(cls, dirhams: float) -> float:
        """Convertit des dirhams en euros (méthode de classe)."""
        return dirhams / cls.taux_eur_dh


# ===== TEST =====
# Appel direct sur la classe : aucune instance nécessaire
print(Convertisseur.vers_dh(100))        # 100 x 10.9 = 1090.0

Convertisseur.changer_taux(11.0)         # le taux devient 11.0
print(Convertisseur.depuis_dh(110))      # 110 / 11.0 = 10.0

# Possible aussi via une instance, même si ce n'est pas nécessaire
conv = Convertisseur()
print(conv.vers_dh(50))                  # 50 x 11.0 = 550.0 (le nouveau taux est utilisé)