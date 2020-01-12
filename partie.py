__authors__ = "Manel Hmidi et Komti Abdelkader"
__date__ = "05/01/2020"

"""Ce fichier permet de modéliser une partie de jeu entre deux joueurs """

from plateau import Plateau
from joueur import Joueur


class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()  # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []  # La liste des deux joueurs (initialement une liste vide).
        # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
        # Pendant le jeu et à chaque tour d'un joueur,
        # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        print("Bienvenue au jeu Tic Tac Toe.\n---------------Menu---------------")
        print("1- Jouer avec l'ordinateur.\n2- Jouter avec une autre personne.")
        print("0- Quitter.\n-----------------------------------")

        choix = self.saisir_nombre(0, 2)
        if choix == 1:
            nom = input("Entrez s.v.p votre nom:?")
            type = "Personne"
            pion = self.demander_forme_pion()
            j1 = Joueur(nom, type, pion)
            if j1.pion.upper() == "X":
                pion2 = "O"
            else:
                pion2 = "X"
            self.joueurs.append(j1)
            j2 = Joueur("Colosse", "Ordinateur", pion2)
            self.joueurs.append(j2)
            x = "O"
            while x.upper() == "O":
                self.plateau.initialiser()
                print(self.plateau)
                while self.plateau.non_plein():
                    self.joueur_courant = self.joueurs[0]
                    self.tour(int(choix))
                    if self.plateau.est_gagnant(pion) or not self.plateau.non_plein():
                        break
                    print("c'est le tour maintenant de l'ordinateur colosse!")
                    self.joueur_courant = self.joueurs[1]
                    self.tour(int(choix))
                    if self.plateau.est_gagnant(pion2) or not self.plateau.non_plein():
                        break
                if self.plateau.est_gagnant(pion):
                    self.joueurs[0].nb_parties_gagnees = self.joueurs[0].nb_parties_gagnees + 1
                    print("Partie terminée! Le joueur gagnant est:", self.joueurs[0].nom)
                elif self.plateau.est_gagnant(pion2):
                    self.joueurs[1].nb_parties_gagnees = self.joueurs[1].nb_parties_gagnees + 1
                    print("Partie terminée! Le joueur gagnant est:", self.joueurs[1].nom)
                else:
                    print("Partie terminée! aucun joueur n'a gagne")
                    self.nb_parties_nulles = self.nb_parties_nulles + 1
                print("Parties gagnées par ", self.joueurs[0].nom, self.joueurs[0].nb_parties_gagnees)
                print("Parties gagnées par ", self.joueurs[1].nom, self.joueurs[1].nb_parties_gagnees)
                print("Parties nulles:", self.nb_parties_nulles)
                x = input("voulez vous recommencez (O,N)?")
                assert isinstance(x, str)
                assert x.upper() in ["O", "N"]
            if x.upper() == "N":
                print("***Merci et Au Revoir***")
                return
        elif choix == 2:
            nom = input("Entrez s.v.p votre nom:?")
            type = "Personne"
            pion = self.demander_forme_pion()
            j1 = Joueur(nom, type, pion)
            self.joueurs.append(j1)
            if j1.pion.upper() == "X":
                pion2 = "O"
            else:
                pion2 = "X"
            nom = input("Entrez s.v.p le nom de l'autre joueur:?")
            type = "Personne"
            j2 = Joueur(nom, type, pion2)
            self.joueurs.append(j2)
            x = "O"
            while x.upper() == "O":
                self.plateau.initialiser()
                print(self.plateau)
                while self.plateau.non_plein():
                    self.joueur_courant = self.joueurs[0]
                    self.tour(int(choix))
                    if self.plateau.est_gagnant(self.joueur_courant.pion) or not self.plateau.non_plein():
                        break
                    print("c'est le tour maintenant du deuxieme joueur!")
                    self.joueur_courant = self.joueurs[1]
                    self.tour(int(choix))
                    if self.plateau.est_gagnant(self.joueur_courant.pion) or not self.plateau.non_plein():
                        break
                if self.plateau.est_gagnant(self.joueur_courant.pion):
                    if self.joueur_courant.nom == self.joueurs[0].nom:
                        self.joueurs[0].nb_parties_gagnees = self.joueurs[0].nb_parties_gagnees + 1
                        print("Partie terminée! Le joueur gagnant est:", self.joueurs[0].nom)
                    else:
                        self.joueurs[1].nb_parties_gagnees = self.joueurs[1].nb_parties_gagnees + 1
                        print("Partie terminée! Le joueur gagnant est:", self.joueurs[1].nom)
                else:
                    print("Partie terminée! aucun joueur n'a gagne")
                    self.nb_parties_nulles = self.nb_parties_nulles + 1
                print("Parties gagnées par ", self.joueurs[0].nom, self.joueurs[0].nb_parties_gagnees)
                print("Parties gagnées par ", self.joueurs[1].nom, self.joueurs[1].nb_parties_gagnees)
                print("Parties nulles:", self.nb_parties_nulles)
                x = input("voulez vous recommencez (O,N)?")
                assert isinstance(x, str)
                assert x.upper() in ["O", "N"]
            if x.upper() == "N":
                print("***Merci et Au Revoir***")
                return

        elif choix == 0:
            print("***Merci et Au revoire***")
            return

    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        test = False
        while test == False:
            print("Entrez s.v.p. un nombre entre ", nb_min, " et ", nb_max, ":?")
            x = input()
            y = int(x)
            if x.isnumeric():
                if y <= nb_max and y >= nb_min:
                    test = True

        return int(x)

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        test = False
        while test == False:
            x = input("Sélectionnez S.V.P la forme du votre pion(x,o):?")
            if x.isalpha():
                if x.upper() == "X" or x.upper() == "O":
                    test = True
        return x.upper()

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."
        if choix == 1:
            if self.joueur_courant.type == "Ordinateur":
                if self.joueur_courant.pion.upper() == "X":
                    pion2 = "O"
                else:
                    pion2 = "X"
                a, b = self.plateau.choisir_prochaine_case(pion2)
            else:
                a, b = self.demander_postion()
        else:
            a, b = self.demander_postion()
        self.plateau.selectionner_case(a, b, self.joueur_courant.pion)
        print(self.plateau)

    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        test = False
        while not test:

            print(self.joueur_courant.nom, " : Entrez s.v.p. les coordonnées de la case à utiliser:")
            print("numéro de la ligne:", end=" ")
            l = int(self.saisir_nombre(0, 2))
            print("numéro de la colonne:", end=" ")
            c = int(self.saisir_nombre(0, 2))
            if self.plateau.position_valide(l, c):
                test = True
                return l, c
            else:
                print("***Valeur Incorrecte***")


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()
