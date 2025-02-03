class UnoCarte:

    def __init__(self, type, couleur):
        self.Type = type
        self.Couleur = couleur

class UnoJeu:

    def Afficher(self):
        print("La carte est une carte ", str(self.Type), " de couleur ", self.Couleur)