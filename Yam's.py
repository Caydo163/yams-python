# Importation
from random import randint
import fileinput
import sys
from turtle import home
from datetime import datetime


class Yams:
    def __init__(self):
        self.grille = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "Brelan": 0,
                       "Carré": 0, "Full": 0, "Petite suite": 0, "Grande suite": 0, "Yam's": 0, "Chance": 0}
        self.total = [0, 0, 0, False]
        self.listeDe = []
        print("\n\n╔══════════════════════════════════════════════════════════╗")
        print("║ ┌──────────────────────────────────────────────────────┐ ║")
        print("║ │            BIENVENUE DANS LE JEU DU YAM'S            │ ║")
        print("║ └──────────────────────────────────────────────────────┘ ║")
        self.home()

    def espace(self, nb=1):
        for i in range(nb):
            print("║                                                          ║")

    def divider(self, nb=2):
        self.espace(2)
        print("╠══════════════════════════════════════════════════════════╣")
        self.espace(nb)

    def home(self):
        self.divider()
        print("║ ┌──────────────────────── MENU ────────────────────────┐ ║")
        print("║ │   1/ JOUER  │  2/ REGLES  │  3/ SCORES | 4/ SORTIR   │ ║")
        print("║ └──────────────────────────────────────────────────────┘ ║")

        rep = 0
        while rep < 1 or rep > 4:
            rep = int(
                input("║  Entrez votre choix : "))
        if rep == 1:
            self.divider()
            self.game()
        elif rep == 2:
            self.divider()
            self.rules()
        elif rep == 3:
            self.divider()
            self.showScore()
        elif rep == 4:
            self.divider()
            print("║ Au revoir ...                                            ║")
            print("╚══════════════════════════════════════════════════════════╝")

    def game(self):
        cpt = 1
        while self.verifEnd() == False:
            print("║ MANCHE", str(cpt).ljust(49), "║")
            self.espace()
            self.showGrid()
            self.diceRoll()
            self.questionChoice()
            self.divider(1)
            cpt += 1
        self.showGrid()
        print("║ Partie terminé !                                         ║")
        name = input("║ Entrer votre nom : ")
        self.saveScore(name, self.total[2])
        print("║ Merci d'avoir joué                                       ║")
        self.espace()
        print("╚══════════════════════════════════════════════════════════╝")

    def rules(self):
        print("║ ┌─────────────────────── REGLES ───────────────────────┐ ║")
        print("║ │                                                      │ ║")
        print('''║ │ Le Yams se  joue  avec 5 dés  et  se finit une  fois │ ║
║ │ toutes les  cases  de  la  fiche de  score remplies. │ ║ 
║ │ Chaque  joueur  joue  tout  à  tour  et dispose de 3 │ ║
║ │ lancers à chaque coup.  L’objectif étant de réaliser │ ║
║ │ des   combinaisons   qui   rapportent  des  points.  │ ║ 
║ │ Le joueur a le choix de reprendre tous ou une partie │ ║
║ │ des dés à chaque  lancé, selon son gré,  pour tenter │ ║
║ │ d’obtenir la combinaison voulue.  A chaque tour,  le │ ║
║ │ joueur doit obligatoirement  inscrire son score dans │ ║
║ │ une des cases de la feuille de  marque que  ce  soit │ ║
║ │ par un X ou par les points qu’il a obtenu.           │ ║''')

        print("║ │                                                      │ ║")

        print('''║ │ Il peut arriver lors  d’un tour  que le  résultat ne │ ║
║ │ convienne  pas  au joueur  et  qu’il  se dise  qu’il │ ║
║ │ pourrait faire un plus grand score sur un autre tour.│ ║
║ │ Il peut alors choisir de barrer une autre case  à la │ ║
║ │ place.  Bien entendu,  il ne pourra plus faire cette │ ║
║ │ combinaison par la suite.                            │ ║''')

        print("║ │                                                      │ ║")

        print('''║ │ Lorsque le total intermédiaire est égal ou supérieur │ ║
║ │ à 63 points,  un bonus de 35 points  supplémentaires │ ║
║ │ est accordé,  ce qui  peut  faire  la différence  au │ ║
║ │ décompte final. Soyez donc stratégique !             │ ║''')

        print("║ │                                                      │ ║")

        print('''║ │ Le gagnant  d’une partie de Yams  est le  joueur qui │ ║
║ │ comptabilisera  le  plus de points à la fin des  10  │ ║
║ │ coups.                                               │ ║''')

        print("║ │                                                      │ ║")

        print("║ └──────────────────────────────────────────────────────┘ ║")

        input("║  Tapez sur 'Entrée' pour quitter ... ")
        self.home()

    def showScore(self):
        print("║ ┌─────────────────────── SCORES ───────────────────────┐ ║")
        print("║ │                                                      │ ║")
        with open("score.txt", "r") as file:
            lines = file.readlines()
        cpt = 1
        space = ""
        for i in lines:
            words = i.split('$')
            print("║ │   "+str(cpt)+"/ " +
                  words[0][1:]+" => "+words[1].ljust(3)+"  ("+words[2][:-1]+")"+space.ljust(27-len(words[0][1:]))+"│ ║")
            cpt += 1

        print("║ │                                                      │ ║")
        print("║ └──────────────────────────────────────────────────────┘ ║")
        input("║  Tapez sur 'Entrée' pour quitter ... ")
        self.home()

    def saveScore(self, name, score):
        check = False
        for line in fileinput.input("score.txt", inplace=1):
            if score > int(line.split('$')[1]):
                line = line.replace(
                    "%", "%"+name+"$"+str(score)+"$"+datetime.today().strftime('%d-%m-%Y')+"\n%")
                sys.stdout.write(line)
                check = True
                break
            sys.stdout.write(line)  # Réécris dans le fichier
        if check == False:
            file = open("score.txt", 'a')
            file.write("%"+name+"$"+str(score)+"$" +
                       datetime.today().strftime('%d-%m-%Y')+"\n")
            file.close()

    def verifPossible(self, choix):
        self.listeDe.sort()
        if choix in [str(i) for i in self.listeDe]:
            return 0

        elif choix.capitalize() == 'Brelan':
            if self.testNbOccurrence(3) != -1:
                return 0
            return 1

        elif choix.capitalize() == 'Carré':
            if self.testNbOccurrence(4) != -1:
                return 0
            return 1

        elif choix.capitalize() == "Yam's":
            if self.listeDe.count(self.listeDe[0]) == len(self.listeDe):
                return 0
            return 1

        elif choix.capitalize() == "Chance":
            return 0

        elif choix.capitalize() == "Grande suite":
            lastI = self.listeDe[0]
            for i in self.listeDe[1:]:
                if i != lastI+1:
                    return 1
                lastI = i
            return 0

        elif choix.capitalize() == "Petite suite":
            check = False
            testListeDe = list(set(self.listeDe))
            if len(testListeDe) < 4:
                return -1
            lastI = testListeDe[0]
            for i in testListeDe[1:-1]:
                if i != lastI+1:
                    check = True
                lastI = i
            lastI = testListeDe[1]
            for i in testListeDe[2:]:
                if i != lastI+1:
                    check = True
                lastI = i
            if check:
                return -1
            return 0

        elif choix.capitalize() == "Full":
            if (self.listeDe[1] != self.listeDe[2] or self.listeDe[2] != self.listeDe[3]) and len(list(set(self.listeDe))) == 2:
                return 0
            return -1

    def testNbOccurrence(self, nbOcc):
        test = self.listeDe[0]
        cpt = 1
        for i in self.listeDe[1:]:
            if i == test:
                cpt += 1
            else:
                test = i
                cpt = 1
            if cpt == nbOcc:
                return 0
        return -1

    def showDice(self):
        self.listeDe.sort()
        print(
            "║    ┌───┬───┬───┬───┬───┐                                 ║\n║    │", end="")
        for i in self.listeDe:
            print("", i, end=" │")
        print("\n║    └───┴───┴───┴───┴───┘                                 ║")

    def diceRoll(self):
        self.listeDe = []
        print("║ Voici votre lancé de dé :                                ║")
        for k in range(5):
            self.listeDe.append(randint(1, 6))
        self.showDice()
        for i in range(2):
            self.espace()
            rep = input(
                "║ Entrez les dés que vous voulez relancer                  ║ \n║ (Entrée pour passez): ")
            if rep == "":
                return
            for j in rep:
                self.listeDe[int(j)-1] = randint(1, 6)
            self.espace()
            print("║ Voici votre nouveau lancé de dé :                        ║")
            self.showDice()

    def showGrid(self):
        chiffre = []
        combo = []
        for key, value in self.grille.items():
            if(key == "Brelan"):
                break
            chiffre.append((key, value))
        for key, value in self.grille.items():
            if(key in "123456"):
                continue
            combo.append((key, value))

        print("║ ┌───────── YAM'S ─────────┐  ┌───────── YAM'S ─────────┐ ║")
        for i in range(7):
            if i == 6:
                if self.total[3] == True:
                    print("║ │ Bonus (> 62)    │ 35    │  │", combo[i][0].ljust(
                        15), "│", str(combo[i][1]).ljust(5), "│ ║")
                else:
                    print("║ │ Bonus (> 62)    │       │  │", combo[i][0].ljust(
                        15), "│", str(combo[i][1]).ljust(5), "│ ║")
            else:
                print("║ │", chiffre[i][0].ljust(15), "│", str(chiffre[i][1]).ljust(
                    5), "│  │", combo[i][0].ljust(15), "│", str(combo[i][1]).ljust(5), "│ ║")

        print("║ ├─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─┤  ├─ ─ ─ ─ ─ ─ ─ ─ ─┼─ ─ ─ ─┤ ║")
        print("║ │ Total supérieur │", str(self.total[0]).ljust(
            5), "│  │ Total inférieur │", str(self.total[1]).ljust(5), "│ ║")
        print("║ └─────────────────────────┘  └─────────────────────────┘ ║")
        print("║ ┌──────────────────────────────────────────────────────┐ ║")
        print("║ │ TOTAL           │", str(self.total[2]).ljust(34), "│ ║")
        print("║ └──────────────────────────────────────────────────────┘ ║")
        self.espace()

    def questionChoice(self):
        choix = 0
        dico = self.possibleChoice()
        self.espace()
        print("║ Choisissez votre combinaison :                           ║")
        if not dico:
            return self.deleteCombination()
        for key in dico:
            print("║ "+str(key)+"/ "+dico[key].ljust(54)+"║")
        while choix > len(dico) or choix < 1:

            choix = int(input("║ --> Entrez votre choix : "))
        self.updatePoint(dico[choix])

    def deleteCombination(self):
        choix = 0
        dico = {}
        cpt = 1
        for key, value in self.grille.items():
            if value == 0:
                dico[cpt] = key
                cpt += 1
        print("║ Vous ne pouvez pas choisir de combinaisons.              ║")
        print("║ Vous devez donc en supprimer une.                        ║")
        for key in dico:
            print("║ "+str(key)+"/ "+dico[key])
        while choix > len(dico) or choix < 1:
            choix = int(input("║ Entrez votre choix : "))
        self.grille[dico[choix]] = "XXXXX"

    def possibleChoice(self):
        dico = {}
        cpt = 1
        for key, value in self.grille.items():
            if value == 0 and self.verifPossible(key) == 0:
                dico[cpt] = key
                cpt += 1
        return dico

    def totalCalcul(self):
        self.total[0] = 0
        self.total[1] = 0
        for key, value in self.grille.items():
            if value != "XXXXX":
                if key in "123456":
                    self.total[0] += value
                else:
                    self.total[1] += value
        if self.total[0] > 62:
            self.total[0] += 35
            self.total[3] = True

        self.total[2] = self.total[0] + self.total[1]

    def verifEnd(self):
        for value in self.grille.values():
            if value == 0:
                return False
        return True

    def updatePoint(self, choix):
        score = 0
        if choix in "123456":
            score = self.listeDe.count(int(choix)) * int(choix)
        elif choix in ["Brelan", "Carré", "Chance"]:
            score = sum(self.listeDe)
        elif choix == "Yam's":
            score = 50
        elif choix == "Petite suite":
            score = 30
        elif choix == "Grande suite":
            score = 40
        elif choix == "Full":
            score = 25

        self.grille[choix] = score
        self.totalCalcul()


partie = Yams()
