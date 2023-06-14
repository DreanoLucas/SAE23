from turtle import *
from random import *


#### GENERATION DE BATEAU ####

def verification_generation_bateau_(bateaux):
    compteur = {}
    # ---            
    for b in bateaux:
        for position in b:
            if position in compteur:
                compteur[position]=+1
            else:
                compteur[position]=1
    # ---            
    for k in compteur:
        if compteur[k]>1:
            return False 
    # ---            
    return True 

def generation_bateau(): #generation aleatoire de bateaux à partir d'une liste de bateaux possibles
    print("###########GENERATION DES BATEAUX EN COURS#############")
    petit_bateau = [[('C','3'), ('D','3')],  [('D','5'), ('E','5')], [('E','3'), ('E','2')],  [('C','3'), ('B','3')], [('E','4'), ('D','4')],  [('C','1'), ('C','2')] ]
    grand_bateau = [[('A','1'),('A','2'), ('A','3')],[('B','4'),('C','4'), ('D','4')],
                    [('B','4'),('B','2'), ('B','3')],[('A','4'),('B','4'), ('C','4')], 
                    [('B','4'),('C','4'), ('A','4')], [('E','2'), ('B','2')], 
                      [('A','3'), ('A','2')], [('C','2'), ('B','2')],  [('D','1'), ('E','1')]]

    bateau_1=grand_bateau[randint(0,len(grand_bateau)-1)] #generation du premier bateau
    bateau_2=petit_bateau[randint(0,len(petit_bateau)-1)] #generation du deuxieme bateau
    bateau_3=petit_bateau[randint(0,len(petit_bateau)-1)] #generation du troisieme bateau

    bateaux = [ bateau_1,bateau_2,bateau_3]

    if verification_generation_bateau_ == False:
        generation_bateau()

    print('HERE',bateaux)

    return bateaux 

####FIN DE LA GENERATION####

def saisie_coordonnees_joueur(entetes_colonnes, entetes_lignes): 
    try:
        rep = input("Coordonnees (p.e. C3) ? ")
        assert(len(rep)==2) #la coordonnees doit contenir 2 caractères
        assert(rep[0].upper() in entetes_colonnes) #le premier caractère doit etre dans entetes_colonnes
        assert(rep[1] in entetes_lignes) #le deuxieme caractère doit etre dans entetes_lignes
        return (rep[0].upper(),rep[1])
    except: # exception « ValueError », les coordonnees ne sont pas valides
        print(f"Désolé mais n'est {rep} pas une coordonnées valide") 
        rep_correcte = saisie_coordonnees_joueur(entetes_colonnes, entetes_lignes)
        return(rep_correcte)

def fabrique_traducteur_positions(origine, taille, entetes_colonnes, entetes_lignes):  #associe les coordonnées du jeu et les coordonnées turtle
    Traducteur_position = {}
    (x0,y0)=origine
    for i in range (len(entetes_colonnes)): 
        C = entetes_colonnes[i] #entete colonne
        x = x0 + taille * i #coordonnes tortue sur l'axe x en fonction de l'entete colonne
        for j in range(len(entetes_lignes)):
            L = entetes_lignes[j] #entete ligne
            y = y0 - taille * j #coordonnes tortue sur l'axe y en fonction de l'entete ligne
            key = (C,L) #clé du dictionnaire = valeur du jeu
            val = (x,y) #valeur du dictionnaire = valeur tortue
            Traducteur_position[key] = val #création du dico
    return Traducteur_position


def fabrique_navires_et_grille(entetes_colonnes, entetes_lignes): #fabrication de la grille depuis la longueur des entetes données
    navires = generation_bateau()
    grille = {}
    for c in entetes_colonnes:
        for l in entetes_lignes:
            key = (c,l)
            grille[key] = False
    for navire in navires:
        for xy in navire:
            grille [xy] = True
    return(navires,grille)



def deplace_proprement(pos): #permet de se deplacer sans que turtle écrive
    up()
    goto(pos)
    down()
################################################################## CREATION DE LA GRILLE ##################################
def trace_carre(pos, taille, plein, couleur):
    deplace_proprement(pos)
    if plein == True:
        fillcolor(couleur)
        begin_fill()
        for i in range (4):
            forward(taille)
            right(90)
        end_fill()
    else:
        for i in range (4):
            forward(taille)
            right(90)

def trace_carre2(pos, taille, plein, couleur):
    x=pos[0]
    y=pos[1]+taille
    xy=(x,y)
    deplace_proprement(xy)
    if plein == True:
        fillcolor(couleur)
        begin_fill()
        for i in range (4):
            forward(taille)
            right(90)
        end_fill()
    else:
        for i in range (4):
            forward(taille)
            right(90)

    
def trace_barre_horizontale(pos, taille, plein, couleur, nb_colonnes): #Trace une barre horizontale
    for i in range(nb_colonnes):   
        x = pos[0] + taille*i
        y = pos[1] + taille*1
        xy=(x,y) 
        trace_carre(xy,taille,plein,couleur)


def trace_barre_verticale(pos, taille, plein, couleur, nb_lignes): #Cree la grille
    x=pos[0]
    for i in range(nb_lignes):
        y=pos[1]-taille*i
        xy=(x,y)
        trace_barre_horizontale(xy,taille,plein,couleur,nb_lignes)

        
def trace_grille_carres(pos, taille, plein, couleur, nb_lignes, nb_colonnes): #Creation de la premiere ligne puis de toute la grille
    print("###########GENERATION DES LA GRILLE EN COURS###########")
    deplace_proprement(pos)
    trace_barre_horizontale(pos,taille,plein,couleur,nb_colonnes) 
    trace_barre_verticale(pos,taille, plein, couleur, nb_lignes)

def trace_entetes_colonnes(pos, taille, entetes_colonnes): #Ecriture des chiffre
    deplace_proprement(pos)
    for i in range(len(entetes_colonnes)):
        x=taille*i+pos[0]+(taille/2)
        y=pos[1]+taille
        xy=(x,y)
        deplace_proprement(xy)
        write(entetes_colonnes[i])

def trace_entetes_lignes(pos, taille, entetes_lignes): #Ecriture des lettres
    deplace_proprement(pos)
    for i in range(len(entetes_lignes)):
        x=pos[0]-(taille/4)
        y=pos[1]-taille*i+taille/3
        xy=(x,y)
        deplace_proprement(xy)
        write(entetes_lignes[i])

################################### Mettre fin a la partie ########################################

def find_dict_with_default(dict, key, default): 
    if key in dict.keys():
        return dict[key]
    else:
        return default

def for_all(Keys, Dico):
    # ---            
    for key in Keys: 
        if find_dict_with_default(Dico,key,False) == False:
            return False        
    # ---            
    return True



def annoncer_si_navire_vient_de_couler(navires_en_vie, devinees, grille): #Enleve les navires devinees de navire_en_vie et annonce lorsque un bateau est entierement decouvert
    for navire in navires_en_vie:
        if for_all(navire, devinees) == True:
            navires_en_vie.remove(navire) 
            print("Navire coulé")
    return navires_en_vie

################## Definition des fins #########################################

def final(): #Si on gagne
    print("Bravo, vous avez coulé tous les navires !")
    clearscreen()
    screen = Screen()
    screen.bgpic("image/gagne1.png")
    screen.screensize(640,381)
    avancer(300,'''C'est gagne''')
    input("Entree pour quitter")
    hideturtle()

def perdu(): #Si on perds
    print("C'est rate...")
    clearscreen()
    screen = Screen()
    screen.bgpic("image/perdu.png")
    screen.screensize(640,381)
    avancer(300,'''Retente une prochaine fois''')
    input("Entree pour quitter")
    hideturtle()
   
def avancer(x,lettre): 
    hideturtle()
    left(90)
    up()
    forward(x)
    down()
    write(lettre,False,font=("arial",20,"normal"))



def test(entetes_lignes,entetes_colonnes):
    x=0 
    y=0 
    print(entetes_lignes[:len(entetes_lignes)- 1])
    #print(zip(len(entetes_colonnes)-3, len(entetes_lignes)-3))
    petit_bateau = [[(y,x+1), (y, x+2)] for x in (range(len(entetes_colonnes)-1)) for y in (entetes_lignes[:len(entetes_lignes)- 1])]
    print((petit_bateau))

test("ABCDE","12345")
