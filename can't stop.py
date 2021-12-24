from tkinter import *
from random import *



#initialisation fenêtre
root = Tk()
root.title("Can't Stop") #
root.geometry("1920x1080")
root.minsize(1080, 800)
root.config(background='#FFFFF0')

#initialisation canvas
canvas_jeu = Canvas(root, width = 700, height = 700, bg = 'ivory')
canvas_jeu.grid(row=0, column=0, sticky=W) #placement du canvas pour qu'il soit à gauche


#création frame pour l'interface homme-machine
frame = Frame(root, bg="#FFFFF0",  relief=SUNKEN)
label_title = Label(frame, text="Bienvenue sur Can't Stop", bg="#FFFFF0", font=("Courrier", 40))
label_title.pack()
frame.grid(row=0, column=1, sticky=NE)
#création frame pour le placement des boutons ( sous frame de la frame ci-dessus )
frame_buttons = Frame(root, bg="#FFFFF0", bd=1, relief=SUNKEN)
frame_buttons.grid(row=0, column=1, sticky=E)
#création frame pour les textes sur les joueurs
frame_joueurs = Frame(root, bg="#FFFFF0", relief=SUNKEN)
frame_joueurs.grid(row=0, column=2, sticky=NE)
#création frame pour les dés
frame_des = Frame(root, bg="#FFFFF0", relief=SUNKEN)
frame_des.grid(row=0, column=1, sticky=NE)

def detruire_bouttons():
    frame_buttons.grid_forget()
    label_title.pack_forget()
    
def detruire_choix_des(paire_1, paire_2, paire_3):
    paire_1.grid_forget()
    paire_2.grid_forget()
    paire_3.grid_forget()
    #frame_des.grid_forget()
    frame.grid_forget()




###CREATION DES CLASSES###

class COLONNE:
    """ création d'une colonne comportant les parametres suivant :
        -- Le numéro de la colonne.
        -- Le nb de case de la colonne.
        -- si il y a un pion noir dessus (True = il y en a un, False = il n'y en a pas).
        -- la position du pion noir (tmp) (0 = pas de pion, 1 à 13 = position sur la grille).
        -- la position des pions de couleur de chaque joueur (0 = pas de pion, 1 à 13 = position sur la grille).
        -- Si la colonne à déjà été gagnée.
        """
    def __init__(self, numero_colonne : int, nb_cases : int, pion_noir : bool, position_tmp : int, position_rouge : int, position_bleu : int, position_vert : int, position_jaune : int, colonne_gagnee : bool):
        self.numero_colonne : int = numero_colonne
        self.nb_cases : int = nb_cases
        self.pion_noir : bool = pion_noir
        self.position_tmp : int = position_tmp
        self.position_rouge : int = position_rouge
        self.position_bleu : int = position_bleu
        self.position_vert : int = position_vert
        self.position_jaune : int = position_jaune
        self.colonne_gagnee : bool = colonne_gagnee
    def __repr__(self) -> str:
        #affichage
        return("COLONNE(" + str(self.numero_colonne) + "," + str(self.nb_cases) + "," + str(self.pion_noir) + "," + str(self.position_tmp) + "," + str(self.position_rouge) + "," + str(self.position_bleu) + "," + str(self.position_vert) + "," + str(self.position_jaune) + "," + str(self.colonne_gagnee) + ")")


class Joueur:
    """ création d'un joueur comportant les parametres suivant:
        -- Le nom du joueur.
        -- La couleu du joueur.
        -- Combien de colonnes il a gagnée.
        """
    def __init__(self, pseudo : str, couleur : str, nb_colonne_gagnee : int):
        self.pseudo : str = pseudo
        self.couleur : str = couleur
        self.nb_colonne_gagnee : int = nb_colonne_gagnee
    def __repr__(self) -> str:
        #affichage
        return("Joueur(" + str(self.pseudo) + ","+ str(self.couleur) + "," + str(self.nb_colonne_gagnee) + ")")
    
###FIN CREATION CLASSES###


###PARTIE CHOIX DES JOUEURS###
    
def choix_joueurs(nb_joueurs : int):
    """
    #Premet la création d'une liste de 2 à 4 joueurs chaqu'un associé à une couleur dans l'ordre Rouge, Bleu, Vert, Jaune puis lance le jeu.
    """
    liste_joueurs : list = [] 
    for i in range(nb_joueurs ):
        if i == 0:
            couleur : str = "Rouge"
            pseudo : str = "Joueur 1"
            joueur_1 = Label(frame_joueurs, text="Le joueur 1 est rouge", bg='red', font=("Courrier", 20))
            joueur_1.pack()
        elif i == 1:
            couleur : str = "Bleu"
            pseudo : str = "Joueur 2"
            joueur_2 = Label(frame_joueurs, text="Le joueur 2 est bleu", bg='blue', font=("Courrier", 20))
            joueur_2.pack()
        elif i == 2:
            couleur : str = "Vert"
            pseudo : str = "Joueur 3"
            joueur_3 = Label(frame_joueurs, text="Le joueur 3 est vert", bg='green', font=("Courrier", 20))
            joueur_3.pack()
        elif i == 3:
            couleur : str = "Jaune"
            pseudo : str = "Joueur 4"
            joueur_4 = Label(frame_joueurs, text="Le joueur 4 est jaune", bg='yellow', font=("Courrier", 20))
            joueur_4.pack()
        joueur = Joueur(pseudo, couleur, 0)
        liste_joueurs.append(joueur)
        deroulement_tour(initialisation(), former_paires(), liste_joueurs, liste_joueurs[0], 4) #On commence le déroulement du jeu quand le choix des joueurs a été fait. 
    

###FIN PARTIE CHOIX DES JOUEURS###



def initialisation() -> list :
    """
    #S'execute un unique fois lors du lancement du jeu afin de créer le pateau.
    >>> initialisation()
    [3, 0, COLONNE(2,3,False,0,0,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,False,0,0,0,0,0,False), COLONNE(5,9,False,0,0,0,0,0,False), COLONNE(6,11,False,0,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    """
    pions_noir_dispo : int = 3
    colonne2 = COLONNE(2,3,False,0,0,0,0,0,False)
    colonne3 = COLONNE(3,5,False,0,0,0,0,0,False)
    colonne4 = COLONNE(4,7,False,0,0,0,0,0,False)
    colonne5 = COLONNE(5,9,False,0,0,0,0,0,False)
    colonne6 = COLONNE(6,11,False,0,0,0,0,0,False)
    colonne7 = COLONNE(7,13,False,0,0,0,0,0,False)
    colonne8 = COLONNE(8,11,False,0,0,0,0,0,False)
    colonne9 = COLONNE(9,9,False,0,0,0,0,0,False)
    colonne10 = COLONNE(10,7,False,0,0,0,0,0,False)
    colonne11 = COLONNE(11,5,False,0,0,0,0,0,False)
    colonne12 = COLONNE(12,3,False,0,0,0,0,0,False)
    plateau = [pions_noir_dispo,0,colonne2,colonne3,colonne4,colonne5,colonne6,colonne7,colonne8,colonne9,colonne10,colonne11,colonne12]
    return(plateau)




########################################################################### PARTIE SUR LES DES ############################################################################################
def former_paires() -> list:
    """
    Permet de créer les paires que le joueur pourra utiliser et en fait une liste.
    """
    des = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
    paire1 = [des[0] + des[1], des[2] + des[3]]
    paire2 = [des[0] + des[2], des[1] + des[3]]
    paire3 = [des[0] + des[3], des[2] + des[1]]
    liste_paires = [paire1, paire2, paire3]
    return liste_paires




def action_des_paires(liste_paires : list, plateau : list) -> list:
    """
    #Permet de lister les actions possible pour chaque nombre de chaque paire. Il y a trois actions possibles.
    #-- "ajout_pion" = On peut ajouter un pion noir à la colonne.
    #-- "avancer_pion" = Un pion et déjà présent sur la colonne, on peut donc l'avancer.
    #-- "colonne_déjà_gagnée" = La colonne est déjà gagnée par un joueur, elle est donc bloquée.
    >>> liste_paires = [[4,5],[3,6],[6,3]]
    >>> plateau = [3, 0, COLONNE(2,3,False,0,0,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,False,0,0,0,0,0,True), COLONNE(5,9,True,2,0,0,0,0,False), COLONNE(6,11,True,1,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    >>> action_des_paires(liste_paires, plateau)
    [['colonne_déjà_gagnée', 'avancer_pion'], ['ajout_pion', 'avancer_pion'], ['avancer_pion', 'ajout_pion']]
    """ 
    liste_actions : list = [] #Liste les actions à efectuer en fonction de la paire choisie.
    for i in range(3): #repete la fonction pour chaque paires.
        paire : list = liste_paires[i] #Extrait la paire de la liste des paires.
        action_paire : list = [] #Sera retouner à la fin du programme.
        chiffre1 : int = paire[0] #Le premier chiffre de la paire.
        chiffre2 : int = paire[1] #Le second chiffre de la paire.
        colonne_du_1 : COLONNE = plateau[chiffre1] #la colonne correspondante au chiffre1.
        colonne_du_2 : COLONNE = plateau[chiffre2] #la colonne correspondante au chiffre2.
        if colonne_du_1.colonne_gagnee == True: #Si la première colonne à déjà été gagnée.
            if colonne_du_2.colonne_gagnee == True: #Et si la deuxième colonne à déjà été gagnée.
                action_paire = ["colonne_déjà_gagnée","colonne_déjà_gagnée"]
            elif colonne_du_2.pion_noir == False: #Et s'il y a un pion noir sur la deuxième colonne.
                action_paire = ["colonne_déjà_gagnée","ajout_pion"]
            else: #Et s'il n'y a pas de pion noir sur la deuxième colonne.
                action_paire = ["colonne_déjà_gagnée","avancer_pion"]
        elif colonne_du_1.pion_noir == False: #S'il y a un pion noir sur la première colonne.
            if colonne_du_2.colonne_gagnee == True: #Et si la deuxième colonne à déjà été gagnée.
                action_paire = ["ajout_pion","colonne_déjà_gagnée"]
            elif colonne_du_2.pion_noir == False: #Et s'il y a un pion noir sur la deuxième colonne.
                action_paire = ["ajout_pion","ajout_pion"]
            else: #Et s'il n'y a pas de pion noir sur la deuxième colonne.
                action_paire = ["ajout_pion","avancer_pion"]
        else: #S'il n'y a pas de pion noir sur la première colonne.
            if colonne_du_2.colonne_gagnee == True: #Et si la deuxième colonne à déjà été gagnée.
                action_paire = ["avancer_pion","colonne_déjà_gagnée"]
            elif colonne_du_2.pion_noir == False: #Et s'il y a un pion noir sur la deuxième colonne.
                action_paire = ["avancer_pion","ajout_pion"]
            else: #Et s'il n'y a pas de pion noir sur la deuxième colonne.
                action_paire = ["avancer_pion","avancer_pion"]
        liste_actions.append(action_paire) 
    return liste_actions




def analyse_des_paires(liste_actions : list, plateau : list) -> list:
    """ 
    #Permet d'analyser la validitée de chaque paire. Il y a trois résultats possibles.
    #-- True = La paire est valide et on réalise une ou les actions corespondantes.
    #-- "Choix" = Les deux actions sont réalisables mais pas en même temps. Il faut donc faire un choix.
    #-- False = La paire n'est pas valide, aucune des deux actions ne peut être effectuée.
    >>> liste_actions = [['colonne_déjà_gagnée', 'avancer_pion'], ['ajout_pion', 'avancer_pion'], ['avancer_pion', 'ajout_pion']]
    >>> plateau = [1, 0, COLONNE(2,3,False,0,0,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,False,0,0,0,0,0,True), COLONNE(5,9,True,2,0,0,0,0,False), COLONNE(6,11,True,1,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    >>> analyse_des_paires(liste_actions, plateau)
    [True, True, True]
    """
    validité : list = [] #Sera retouner à la fin du programme.
    pions_noirs_dispo : int = plateau[0]
    for i in range(3): #Pour chaques paires d'actions contenu dans "liste_actions".
        actions_paire : list = liste_actions[i]
        if pions_noirs_dispo == 3 or pions_noirs_dispo == 2: #il y a 2 ou 3 pions noirs non utilisé.
            if actions_paire[0] == "colonne_déjà_gagnée" and actions_paire[1] == "colonne_déjà_gagnée": #Si les 2 colonnes ont déjà été gagnées, la paire n'est pas valide.
                validité.append(False)
            else: #Sinon la paire est valide
                validité.append(True)
        elif pions_noirs_dispo == 1: #Il n'y a plus qu'un pion noir non utilisé.
            if actions_paire[0] == "ajout_pion" and actions_paire[1] == "ajout_pion": #S'il faut ajouter un pion noir sur les deux colonnes, la paire et valide mais le joueur doit choisir la colonne.
                validité.append("Choix")
            elif actions_paire[0] == "colonne_déjà_gagnée" and actions_paire[1] == "colonne_déjà_gagnée": #Si les 2 colonnes ont déjà été gagnées, la paire n'est pas valide.
                validité.append(False)
            else: #Sinon la paire et valide.
                validité.append(True)
        else: #Tous les pions noirs ont été utilisés.
            if actions_paire[0] == "avancer_pion" or actions_paire[1] == "avancer_pion": #S'il faut avancer le pion sur l'une des deux colonnes, la paire est valide.
                validité.append(True)
            else: #Sinon, elle ne l'est pas.
                validité.append(False)
    return validité




###FIN PARTIE SUR LES DES###
def callback1(plateau, liste_paires ,liste_joueurs, joueur, action): #fonctions qui permettent d'appeler le deroulement du tour en fonction de l'action chosie
    action : int = 1
    deroulement_tour(plateau, liste_paires ,liste_joueurs, joueur, action)
    

def callback2(plateau, liste_paires ,liste_joueurs, joueur, action):
    action : int = 2
    deroulement_tour(plateau, liste_paires ,liste_joueurs, joueur, action)
    

def callback3(plateau, liste_paires ,liste_joueurs, joueur, action):
    action : int = 3
    deroulement_tour(plateau, liste_paires, liste_joueurs, joueur, action)
    
    
def callback4(plateau, liste_paires ,liste_joueurs, joueur, action):
    action : int = 0
    deroulement_tour(plateau, liste_paires , liste_joueurs, joueur, action)




def Choix_action(plateau : list,liste_paires : list, validite_des_paires : list, liste_joueurs : list, joueur : Joueur, action : int) -> int:
    """Propose les differentes paire au joueur et attend qu'il en choisisse une ou qu'il passe son tour en fonction du resultat d'analyse_des_paires.
    Il faut donc afficher les paires si elles sont valides ainsi que "Passer son tour". 
    Le programme doit retourner 0 si le joueur passe son tour ou 1, 2 ou 3 en fonction de la paire choisie par le joueur. """
    paire_1 = Button(frame_des, text=str(liste_paires[0]), bg="#FFFFF0", font=("Courrier", 40), command = lambda:[detruire_choix_des(paire_1, paire_2, paire_3), callback1(plateau,  liste_paires, liste_joueurs, joueur, action)])
    paire_2 = Button(frame_des, text=str(liste_paires[1]), bg="#FFFFF0", font=("Courrier", 40), command = lambda:[detruire_choix_des(paire_1, paire_2, paire_3), callback2(plateau,  liste_paires, liste_joueurs, joueur, action)])
    paire_3 = Button(frame_des, text=str(liste_paires[2]), bg="#FFFFF0", font=("Courrier", 40), command = lambda:[detruire_choix_des(paire_1, paire_2, paire_3), callback3(plateau,  liste_paires, liste_joueurs, joueur, action)])
    passer_tour = Button(frame_des, text="passer le tour", bg="#FFFFF0", font=("Courrier", 40), command = lambda:[detruire_choix_des(paire_1, paire_2, paire_3), callback4(plateau, liste_paires, liste_joueurs, joueur, action)])
    if validite_des_paires[0] == True and validite_des_paires[1] == True and validite_des_paires[2] == True: 
        paire_1.grid(row=1, column=1, sticky=S) 
        paire_2.grid(row=2, column=1, sticky=S)
        paire_3.grid(row=3, column=1, sticky=S)
    elif validite_des_paires[0] == True and validite_des_paires[1] == True: #and validite_des_paires[2] == False: #les trois autres cas
        paire_1.grid(row=1, column=1, sticky=S)
        paire_2.grid(row=2, column=1, sticky=S)
    elif validite_des_paires[0] == True and validite_des_paires[2] == True: #and validite_des_paires[1] == False:
        paire_1.grid(row=1, column=1, sticky=S)
        paire_2.grid(row=2, column=1, sticky=S)
    elif validite_des_paires[1] == True and validite_des_paires[2] == True: #and validite_des_paires[0] == False:
        paire_1.grid(row=1, column=1, sticky=S)
        paire_2.grid(row=2, column=1, sticky=S)
    
    passer_tour.grid(row=4, column=1, sticky=S)




def nouveau_tour(plateau : list, liste_paires : list, liste_joueurs : list, joueur : Joueur) -> None:
    """
    Fonction permettant le debut d'un nouveau tour en changant la couleur du joueur dans cet ordre : Rouge -> Bleu -> Vert -> Jaune -> Rouge...
    """
    couleur_joueur : str = joueur.couleur #récupére la couleur de l'ancien joueur.
    if couleur_joueur == "Rouge":
        joueur = liste_joueurs[1] #Le joueur suivant est le Bleu.
    elif couleur_joueur == "Bleu":
        if len(liste_joueurs) > 2:
            joueur = liste_joueurs[2] #Le joueur suivant est le Vert.
        else:
            joueur = liste_joueurs[0] #Le joueur suivant est le Rouge.
    elif couleur_joueur == "Vert":
        if len(liste_joueurs) == 4:
            joueur = liste_joueurs[3] #Le joueur suivant est le Jaune.
        else:
            joueur = liste_joueurs[0] #Le joueur suivant est le Rouge.
    elif couleur_joueur == "Jaune":
        joueur = liste_joueurs[0] #Le joueur suivant est le Rouge.
    plateau[0] = 3
    couleur_joueur = joueur.couleur #récupére la couleur du nouveau joueur.
    for i in range(2,13): #Pour chaque colonne, la position temporaire (du pion noir s'il y en a un) se fixe sur celle du nouveau joueur.
        colonne = plateau[i]
        if couleur_joueur == "Rouge":
            colonne.position_tmp = colonne.position_rouge 
        elif couleur_joueur == "Bleu":
            colonne.position_tmp = colonne.position_bleu 
        elif couleur_joueur == "Vert":
            colonne.position_tmp = colonne.position_vert 
        elif couleur_joueur == "Jaune":
            colonne.position_tmp = colonne.position_jaune
    plateau[i] = colonne 
    creation_plateau(plateau)
    deroulement_tour(plateau, liste_paires,liste_joueurs, joueur, 4)




def deplacement(num_paire : int, plateau : list, liste_paires : list, liste_actions : list, ) -> list:
    """
    #Déplace les pions noir (ou les ajoute) en fonction de la paire choisie par le joueur et des actions qui lui corespondent.
    >>> num_paire = 2
    >>> plateau = [1, 0, COLONNE(2,3,False,0,0,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,False,0,0,0,0,0,True), COLONNE(5,9,True,2,0,0,0,0,False), COLONNE(6,11,True,1,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    >>> liste_paires = [[4,5],[3,6],[6,3]]
    >>> liste_actions = [['colonne_déjà_gagnée', 'avancer_pion'], ['ajout_pion', 'avancer_pion'], ['avancer_pion', 'ajout_pion']]
    >>> deplacement(num_paire, plateau, liste_paires, liste_actions)
    [0, 0, COLONNE(2,3,False,0,0,0,0,0,False), COLONNE(3,5,True,1,0,0,0,0,False), COLONNE(4,7,False,0,0,0,0,0,True), COLONNE(5,9,True,2,0,0,0,0,False), COLONNE(6,11,True,2,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    """
    paire : list = liste_paires[num_paire - 1] #la paire sélectionnée dans "Choix_action".
    actions : list = liste_actions[num_paire - 1] #Les actions corespendantes à la paire sélectionnée.
    chiffre1 : int = paire[0] #Le premier chiffre de la paire.
    chiffre2 : int = paire[1] #Le second chiffre de la paire.
    colonne_du_1 : COLONNE = plateau[chiffre1] #La colonne correspondante au chiffre1.
    colonne_du_2 : COLONNE = plateau[chiffre2] #La colonne correspondante au chiffre2.
    action_chiffre1 : str = actions[0] #L'action correspondante au chiffre1.
    action_chiffre2 : str = actions[1] #L'action correspondante au chiffre1.
    if action_chiffre1 == "ajout_pion" and plateau[0] != 0: #Si l'on doit ajouter un pion noir sur la colonne du chiffre 1.
        colonne_du_1.position_tmp += 1
        colonne_du_1.pion_noir = True #Il y a maintenant un pion noir sur la colonne.
        plateau[0] += -1 #On retire un pion noir de la réserve.
    elif action_chiffre1 == "avancer_pion" and plateau[0] != 0: #Si on doit avancer le pion noir.
        colonne_du_1.position_tmp += 1
    plateau[chiffre1] = colonne_du_1

    if action_chiffre2 == "ajout_pion": #Si l'on doit ajouter un pion noir sur la colonne du chiffre 2.
        colonne_du_2.position_tmp += 1
        colonne_du_2.pion_noir = True #Il y a maintenant un pion noir sur la colonne.
        plateau[0] += -1 #On retire un pion noir de la réserve.
    elif action_chiffre2 == "avancer_pion": #Si on doit avancer le pion noir.
        colonne_du_2.position_tmp += 1
    plateau[chiffre2] = colonne_du_2
    return plateau




def fin_du_tour_voulu(plateau : list, joueur : Joueur) -> list:
    """
    #Execute la fin du tour lorsqu'elle est voulu par le joueur en remplacant les pions noirs par ceux de sa couleur et en comptabilisant le nombre de colonne gagnées.
    >>> plateau = [0, 0, COLONNE(2,3,True,2,0,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,True,3,0,0,0,0,False), COLONNE(5,9,False,0,0,0,0,0,False), COLONNE(6,11,False,0,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,True,2,0,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    >>> fin_du_tour_voulu(plateau, Joueur("Billy","Rouge",0))
    [0, 0, COLONNE(2,3,False,0,2,0,0,0,False), COLONNE(3,5,False,0,0,0,0,0,False), COLONNE(4,7,False,0,3,0,0,0,False), COLONNE(5,9,False,0,0,0,0,0,False), COLONNE(6,11,False,0,0,0,0,0,False), COLONNE(7,13,False,0,0,0,0,0,False), COLONNE(8,11,False,0,2,0,0,0,False), COLONNE(9,9,False,0,0,0,0,0,False), COLONNE(10,7,False,0,0,0,0,0,False), COLONNE(11,5,False,0,0,0,0,0,False), COLONNE(12,3,False,0,0,0,0,0,False)]
    """
    for i in range(2,13): #Pour chque colonne du plateau.
        colonne : COLONNE = plateau[i] #Récupere la colonne étudiée
        if colonne.pion_noir == True: #S'il y a eu un pion noir sur la colonne.
            position_noir : int = colonne.position_tmp #Récupére la position du pion noir.
            if position_noir == colonne.nb_cases: #Si le joueur est arrivé au sommet de la colonne.
                colonne.colonne_gagnee = True
                joueur.nb_colonne_gagnee += 1

            if joueur.couleur == "Rouge": #Si c'étais le tour du joueur Rouge.
                colonne.position_rouge = position_noir
            elif joueur.couleur == "Bleu": #Si c'étais le tour du joueur Bleu.
                colonne.position_bleu = position_noir
            elif joueur.couleur == "Vert": #Si c'étais le tour du joueur Vert.
                colonne.position_vert = position_noir
            elif joueur.couleur == "Jaune": #Si c'étais le tour du joueur Jaune.
                colonne.position_jaune = position_noir

            colonne.position_tmp = 0
            colonne.pion_noir = False
        plateau[i] = colonne
    return plateau




def fin_du_tour_non_voulu(plateau : list) -> list:
    """
Execute la fin du tour lorsqu'elle n'est pas voulu par le joueur en retirant les pions noirs du plateau.
"""
    for i in range(2,13):
        colonne : COLONNE = plateau[i] #Récupere la colonne étudiée
        if colonne.pion_noir == True: #S'il y a eu un pion noir sur la colonne.
            colonne.position_tmp = 0
            colonne.pion_noir == False
        plateau[i] = colonne
    return plateau


def deroulement_tour(plateau : list, liste_paires : list, liste_joueurs : list, joueur : Joueur, action : int) -> None:
    """
    Fonction qui assemble plussieurs fonctions ci-dessus afin de simuler un lancer de dé puis de lancer "nouveau_tour" si le joueur a fini le sien ou "deroulement_tour" lorsqu'il rejoue.
    """
    #creation_plateau(plateau)
    #liste_paires : list = former_paires() #forme les paires
    liste_actions : list = action_des_paires(liste_paires, plateau) #associe les actions au paires
    validite_des_paires : list = analyse_des_paires(liste_actions, plateau) #valide les paires
    if joueur.nb_colonne_gagnee == 3: #Si le joueur a gagné 3 colonnes.
        fin_du_jeu(joueur) #Fin du jeu
    else:
        label_joueur_actif = Label(frame, text=joueur.pseudo, bg="#FFFFF0", font=("Courrier", 40))
        label_joueur_actif.pack()
        Choix_action(plateau, liste_paires, validite_des_paires, liste_joueurs, joueur, action)
        if validite_des_paires[0] == False and validite_des_paires[1] == False and validite_des_paires[2] == False: #Si aucune paire n'est valide
            plateau = fin_du_tour_non_voulu(plateau) #Fin du tour en retirant les pions noir
            creation_plateau(plateau)
            nouveau_tour(plateau, former_paires(), liste_joueurs, joueur) #On débute un nouveau tour.
        else: #Si au moin une paire est valide.
            if action == 0: #Si le joueur à choisi "Fin du tour"
                plateau = fin_du_tour_voulu(plateau, joueur) #Fin du tour en rempacant les pions noir par les pions de la couleur du joueur.
                creation_plateau(plateau)
                nouveau_tour(plateau, former_paires(), liste_joueurs, joueur) #On débute un nouveau tour.
            elif 0 < action < 4: #Si le joueur à séléctionné une des 3 paires.
                plateau = deplacement(action, plateau, liste_paires, liste_actions) 
                creation_plateau(plateau)
                deroulement_tour(plateau, former_paires(),liste_joueurs, joueur, 4) #Il rejoue.
        
        


def fin_du_jeu(joueur : Joueur):
    victoire = Toplevel(root)
    victoire.geometry("800x800")
    label_gagnant = Label(victoire, text=joueur.pseudo + " a gagné !", bg="#FFFFF0", font=("Courrier", 40))
    label_gagnant.pack()



#création du plateau graphiquement ( recréé chaque tour ) 
def creation_plateau(plateau : list):
    canvas_jeu.delete("all") #supprime le contenu du canvas au début de chaque tout pour le refaire en fonction des nouvelles informations 
    cote : int = 50
    ###Création du plateau en lui-même###
    for i in range(2,13):
        cases : int = (plateau[i]).nb_cases #on détermine le nombre de cases de chaque colonne
        x : int = cote*(i-1)
        for j in range(cases): #cases + 1 pour avoir une case où noter le numéro de la colonne
            y : int = 650 - j*cote
            if plateau[i].colonne_gagnee == True: #si la colonne est gagnée on la met d'une certaine couleur
                canvas_jeu.create_rectangle(x, y, x + cote, y + cote,fill="grey")
            else:
                canvas_jeu.create_rectangle(x, y, x + cote, y + cote,fill="#CD8576") #sinon on la remplit de la couleur normale
            
            
        #positionnement des pions###    
        #si il y a un pion noir sur la colonne, on va créer un pion noir à la position voulue
        if plateau[i].pion_noir == True:
            pion_noir = plateau[i].position_tmp - 1
            y : int = 650 - pion_noir*cote #on se rend à la position voulue
            if pion_noir < cases:  #on vérifie  que le pion à placer n'est pas en dehors du plateau
                canvas_jeu.create_circle(x+(cote/2),y+(cote/2), 15, fill="black") #on crée un pion noir
        #si il y a un pion rouge
        if plateau[i].position_rouge > 0:
            pion_rouge = plateau[i].position_rouge -1
            y : int = 650 - pion_rouge*cote #on se rend à la position voulue
            if pion_rouge < cases:
                canvas_jeu.create_circle(x+(cote/2),y+(cote/2), 15, fill="red") #on crée un pion rouge
        #si il y a un pion vert
        if plateau[i].position_vert > 0:
            pion_vert = plateau[i].position_vert -1
            y : int = 650 - pion_vert*cote #on se rend à la position voulue
            if pion_vert < cases:
                canvas_jeu.create_circle(x+(cote/2),y+(cote/2), 15, fill="green") #on crée un pion vert
        #si il y a un pion bleu
        if plateau[i].position_bleu > 0:
            pion_bleu = plateau[i].position_bleu -1
            y : int = 650 - pion_bleu*cote #on se rend à la position voulue
            if pion_bleu < cases:
                canvas_jeu.create_circle(x+(cote/2),y+(cote/2), 15, fill="blue") #on crée un pion bleu
        #si il y a un pion jaune
        if plateau[i].position_jaune > 0:
            pion_jaune = plateau[i].position_jaune -1
            y : int = 650 - pion_jaune*cote #on se rend à la position voulue
            if pion_jaune < cases:
                canvas_jeu.create_circle(x+(cote/2),y+(cote/2), 15, fill="yellow") #on crée un pion jaune
    
          

          
###DIVERS###          
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs) #création d'une fonction circulaire qui n'existe pas dans tkinter de base
Canvas.create_circle = _create_circle
###FIN DIVERS###

def main():
    """
    Fonction principale
    """
    creation_plateau(initialisation())
    #choix joueurs(graphique) 
    deux_joueurs = Button(frame_buttons, text="2 joueurs", bg="#FFFFF0", font=("Courrier", 40), command=lambda:[detruire_bouttons(), choix_joueurs(2)]) #on crée l'appel à la fonction choix_joueurs à l'aide de nos boutons.
    trois_joueurs = Button(frame_buttons, text="3 joueurs", bg="#FFFFF0", font=("Courrier", 40), command=lambda:[detruire_bouttons(), choix_joueurs(3)])
    quatre_joueurs = Button(frame_buttons, text="4 joueurs", bg="#FFFFF0", font=("Courrier", 40), command=lambda:[detruire_bouttons(), choix_joueurs(4)])
    deux_joueurs.grid(row=0, column=1, sticky=E)
    trois_joueurs.grid(row=0, column=2, sticky=E)
    quatre_joueurs.grid(row=0, column=3, sticky=E)
    
main()
        
root.mainloop()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
