from tools2 import *

def jouer():
    speed(1000)
    hideturtle()
    vie=10 #Nombre d'erreurs permises
    # ---
    entetes_colonnes = "ABCDE" # on pourra les changer, en rajouter, les renverser, etc
    entetes_lignes = "12345" # idem
    origine = (-200,200) # coordonnées turtle de l'angle en bas à gauche du carré A1
    taille = 50 # taille en pixels d'une case (côté du carré)
    # ---
    traducteur_positions = fabrique_traducteur_positions(origine, taille, entetes_colonnes, entetes_lignes)
    (navires, grille) = fabrique_navires_et_grille(entetes_colonnes, entetes_lignes)
    # ---
    nb_colonnes = len(entetes_colonnes) # nombre de colonnes
    nb_lignes = len(entetes_lignes) # nombre de lignes
    # ---
    trace_grille_carres(origine, taille, False, "white", nb_lignes, nb_colonnes)
    trace_entetes_colonnes(origine, taille, entetes_colonnes)
    trace_entetes_lignes(origine, taille, entetes_lignes)
    # ---
    devinees = {} # dictionnaire des cases devinées
    navires_en_vie = navires # liste des navires pas encore coulés
    while navires_en_vie != [] :
        (X,Y) = saisie_coordonnees_joueur(entetes_colonnes, entetes_lignes)
        pos = traducteur_positions[(X,Y)] # traduit en position tortue
        if grille[(X,Y)]: # grille est un dictionnaires à valeurs booléennes
            trace_carre2(pos, taille, True, "salmon4") # couleur des navires
            devinees[(X,Y)] = True # la case (X,Y) est devinée
            navires_en_vie = annoncer_si_navire_vient_de_couler(navires_en_vie, devinees, grille)
        else:
            trace_carre2(pos, taille, True, 'darkblue') # couleur de l'eau
            vie = vie-1
            if vie<=3 and vie>1:
                print("Plus que",vie,"erreurs avant de perdre!")
            elif vie==1:
                print('Plus aucune erreur permise!')
        if vie==0:
            break           
    # ---
    if vie!=0:
        final()
    else:
        perdu()

jouer()