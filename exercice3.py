
from abc import ABC, abstractmethod


# Classe abstraite
class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self._montant = float(montant)

    @abstractmethod
    def payer(self):
        pass


# Vérification simplifiée du numéro de carte 
def carte_valide(numero):
    numero = numero.replace(" ", "")

    if not numero.isdigit() or not 13 <= len(numero) <= 19:
        return False

    chiffres = [int(chiffre) for chiffre in numero]
    somme = 0

    for i in range(len(chiffres) - 1, -1, -1):
        chiffre = chiffres[i]

        # Doubler un chiffre sur deux en partant de la droite
        if (len(chiffres) - 1 - i) % 2 == 1:
            chiffre *= 2

            if chiffre > 9:
                chiffre -= 9

        somme += chiffre

    return somme % 10 == 0


# Paiement par carte bancaire
class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not carte_valide(numero):
            raise ValueError("Numéro de carte invalide.")

        if not cvv.isdigit() or len(cvv) not in (3, 4):
            raise ValueError("CVV invalide.")

        self._numero = numero.replace(" ", "")
        self._cvv = cvv

    def payer(self):
        return (
            f"Paiement par carte bancaire confirmé : "
            f"{self._montant:.2f} €."
        )


# Paiement par PayPal
class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Adresse e-mail invalide.")

        if not token.strip():
            raise ValueError("Le token API est obligatoire.")

        self._email = email
        self._token = token

    def payer(self):
        return (
            f"Paiement par PayPal confirmé : "
            f"{self._montant:.2f} € pour {self._email}."
        )


# Paiement en cryptomonnaie
class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id.strip():
            raise ValueError("L'identifiant du portefeuille est obligatoire.")

        reseaux_valides = ("BTC", "ETH")

        if reseau.upper() not in reseaux_valides:
            raise ValueError("Réseau non pris en charge.")

        self._wallet_id = wallet_id
        self._reseau = reseau.upper()

    def payer(self):
        return (
            f"Paiement Crypto ({self._reseau}) confirmé : "
            f"{self._montant:.2f} €."
        )


# Fonction polymorphe
def traiter_paiements(liste):
    print(" Traitement des paiements ")

    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    paiements = [
        CarteBancaire(100, "4532015112830366", "123"),
        CarteBancaire(540.50, "4111111111111111", "456"),

        PayPal(75, "alice@example.com", "TOKEN_ABC"),
        PayPal(120, "bob@example.com", "TOKEN_XYZ"),

        Crypto(50, "WALLET_BTC_001", "BTC"),
        Crypto(200, "WALLET_ETH_002", "ETH")
    ]

    traiter_paiements(paiements)
