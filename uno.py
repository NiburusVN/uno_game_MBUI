"""
Amine Belhaj & Michel Bui
Programme: Uno
Ce programme est une simulation simplifiée du jeu uno avec 2 joueurs.

Pour commencer le programme, il faudra faire une instanciation de la classe UnoJeu depuis la console.
Expemple: jeu = UnoJeu()
On peut ensuite commencer le jeu.
"""

# On importer la librairie random afin de pouvoir choisir alléatoirement qui commencera
import random

# Classe UnoCarte

class UnoCarte:
    def __init__(self, valeur, couleur, estPlus2 = False, estPlus4 = False, estJoker = False):
        """
            Constructeur :
                Crée une nouvelle carte en mettant les propriétés spécifiées à jour.

            Propriétés :
                Valeur (int) : Le numéro de la carte
                Couleur (str) : La couleur de la carte
                EstPlus4 (bool) : True si la carte est un +4, False sinon
                EstPlus2 (bool) : True si la carte est un +2, False sinon
        """
        self.Valeur = valeur
        self.Couleur = couleur
        self.EstPlus4 = estPlus4
        self.EstPlus2 = estPlus2
        self.EstJoker = estJoker

    #
    def __str__(self):

        if self.EstJoker:
            return "\t[Joker]"
        elif self.EstPlus2:
            return "+2\t" + self.Couleur
        elif self.EstPlus4:
            return "+4"
        else:
            return str(self.Valeur) + " \t" + self.Couleur


# Classe UnoJeu, c'est la classe principale du programme, celle avec quoi on va pouvoir jouer

class UnoJeu:
    def __init__(self):
        """
            Constructeur :
                Crée le jeu de cartes.
                Initialise les joueurs 1 et 2
        """
        self.CreerJeu()
        self.J1 = self.InitialiserJoueur()
        self.J2 = self.InitialiserJoueur()


    def AjouterCarteFaceCachee(self, carte):
        """
            Modifications :
                Ajoute la carte donnée aux cartes cachées.
        """
        self.CartesCachees.append(carte)

    def AjouterCarteFaceVisible(self, carte):
        """
            Modifications :
                Ajoute la carte donnée aux cartes visibles.
        """
        self.CartesVisibles.append(carte)

    def InitialiserJoueur(self):
        """
            Résultat :
                Un jeu de 7 cartes piochées sur la pile de cartes cachées.
        """
        jeu = []
        for i in range(7):
           c = self.CartesCachees.pop()
           jeu.append(c)
        return jeu

    def CreerJeu(self):
        """
            Résultat :
                Initialise les cartes cachées avec la composition classique du jeu de Uno.
                Pose une carte face visible.
        """
        # Préparation du jeu
        self.CartesCachees = []
        # Pour chaque couleur existante
        for couleur in ['Rouge', 'Bleu', 'Vert', 'Jaune']:
            # Ajout d'une carte de valeur 0
            c0 = UnoCarte(0, couleur)
            self.AjouterCarteFaceCachee(c0)
            # Ajout des cartes de valeurs 0 à 19
            for i in range(20):
               self.AjouterCarteFaceCachee(UnoCarte(i, couleur))
            # Ajout 2 cartes +2 pour la couleur
            for i in range(2):
                self.AjouterCarteFaceCachee(UnoCarte(None, couleur, estPlus2 = True))


        # Quatre Joker
        for i in range(4):
           self.AjouterCarteFaceCachee(UnoCarte(None, None, estJoker = True))

        # Quatre cartes +4
        for i in range(4):
           self.AjouterCarteFaceCachee(UnoCarte(None, None, estPlus4 = True))

        random.shuffle(self.CartesCachees)

        # Préparation face visible
        self.CartesVisibles = []
        premiereCarte = self.CartesCachees.pop()
        self.AjouterCarteFaceVisible(premiereCarte)

    def AfficherCartesCachees(self):
        """
            Modifications :
                Affiche les cartes cachées.
        """
        for c in self.CartesCachees:
            print(str(c))


    def AfficherCartesVisibles(self):
        """
            Modifications :
                Affiche les cartes visibles.
        """
        for c in self.CartesVisibles:
            print(str(c))

    def MontrerJeuJ1(self):
        """
            Modifications :
                Affiche les cartes du joueur 1, stockées dans self.J1
        """
        for i in range(len(self.J1)):
            print(i, " : ", self.J1[i])

    def MontrerJeuJ2(self):
        """
            Modifications :
                Affiche les cartes du joueur 2, stockées dans self.J2
        """
        for i in range(len(self.J1)):
            print(i, " : ", self.J1[i])

    def DerniereCarteVisible(self):
        """
            Résultat :
                Renvoie la dernière carte posée sur les cartes visibles
        """
        return self.CartesVisibles.copy().pop()


    def MontrerDerniereCarteVisible(self):
        """
            Modifications :
                Affiche la dernière carte posée sur les cartes visibles
        """
        print(self.DerniereCarteVisible())


    def PeutJouer(self, c):
        """
            Résultat :
            Renvoie si oui ou non la carte donnée peut être posée au-dessus
            de la dernière carte visible.
        """
        # Stockons la dernière carte posée dans une variable
        derniereCarte = self.DerniereCarteVisible()
        if c.EstJoker or c.EstPlus4:
            # Si la carte posée est un joker ou un +4, pas de soucis
            return True
        elif c.EstPlus2:
            # Si la carte posée est un +2, on doit juste vérifier la couleur
            if derniereCarte.EstPlus2 or derniereCarte.Couleur == c.Couleur:
                return True
            else:
                return False
        else:
            # La carte posée est une carte classique
            # Intéressons-nous alors à la dernière carte posée
            if derniereCarte.EstPlus4 or derniereCarte.EstJoker:
                # Si c'est un +4 ou un Joker, c'est bon.
                return True
            elif derniereCarte.EstPlus2:
                # Si c'est un +2, on vérifie juste la couleur
                if derniereCarte.Couleur == c.Couleur:
                    return True
                else:
                    return False
            else:
                # Si c'est aussi une carte classique, la valeur ou la couleur
                # doit être la même
                if c.Couleur == derniereCarte.Couleur or c.Valeur == derniereCarte.Valeur:
                    return True
                else:
                    return False

    def J1_Joue(self, i):
        """
            Modifications :
                Permet au joueur 1 de jouer sa carte n°i, seulement s'il peut la
                jouer.
        """
        # Vérification de la présence de la carte (est-ce que cette indice existe ?)
        # Sinon, affiche un message d'erreur.
        try:
            self.J1[i]
        except IndexError:
            return "Cette carte n'existe pas"


        # c définit la carte choisie par le joueur
        c = self.J1[i]
        if self.PeutJouer(c):

            print("Le joueur 1 joue : ", c)

            # Supprimons la carte du jeu du joueur

            del self.J1[i]
            # Ajoutons la à la pioche face visible
            self.AjouterCarteFaceVisible(c)
        else:
            print("Le joueur 1 ne peut pas jouer ", c, " sur", end=" ")
            self.MontrerDerniereCarteVisible()



    def J2_Joue(self, i):
        """
            Modifications :
            Permet au joueur 2 de jouer sa carte n°i, seulement s'il peut la
            jouer.
        """

        # Vérification de la présence de la carte (est-ce que cette indice existe ?)
        # Sinon, affiche un message d'erreur.
        try:
            self.J2[i]
        except IndexError:
            return "Cette carte n'existe pas"


        # c définit la carte choisie par le joueur
        c = self.J2[i]
        if self.PeutJouer(c):

            print("Le joueur 2 joue : ", c)

            # Supprimons la carte du jeu du joueur

            del self.J2[i]
            # Ajoutons la à la pioche face visible
            self.AjouterCarteFaceVisible(c)
        else:
            print("Le joueur 2 ne peut pas jouer ", c, " sur ", end=" ")
            self.MontrerDerniereCarteVisible()

